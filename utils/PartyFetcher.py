#!/usr/bin/python3

__author__ = 'cfilby'

import configparser
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from subprocess import Popen, DEVNULL
from time import sleep

class PartyFetcher:
    """
    The PartyFetcher is used to download the Party CSV data files, which are not a part of a nightly dump like the
    expenditure/contribution data. The Party CSV files contain information such as OrgID, candidate name, the position
    the candidate is running for, etc. Selenium is used since the datafiles must be fetched across two separate form
    submits, one for active and one for dissolved parties. The data itself is downloaded by invoking a JavaScript
    function on that page.
    """

    def __init__(self, config_file):
        """
        Create a new PartyFetcher Object and create a new Selenium webdriver.
        :param config_file:
        :return:
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.destination_dir = self.config["PARTY_FETCHER"]["destination_dir"]
        self.destination_file = self.config["PARTY_FETCHER"]["destination_file"]
        self.server = Popen("java -jar selenium-server-standalone-2.45.0.jar", shell=True, stdout=DEVNULL, stderr=DEVNULL)
        selenium_sleep_time = float(self.config["PARTY_FETCHER"]["selenium_sleep_time"])
        sleep(selenium_sleep_time) # Wait for the server to start up before connecting to it.
        self.driver = webdriver.Remote(
            command_executor= self.config["PARTY_FETCHER"]["selenium_server"],
            desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS
        )

    def get_party_data(self):
        """
        Main method used to download the party data and write it to a single CSV file.
        :return:
        """
        # Fetch the CSV Data
        active_parties = self._get_active_parties()
        inactive_parties = self._get_inactive_parties()

        # Remove the blank last row of both lists, remove the csv header row of inactive_parties and join the lists
        active_parties.pop()
        inactive_parties.pop(0)
        inactive_parties.pop()
        parties = active_parties + inactive_parties

        # Write the csv data
        self._write_csv_file(parties)


    def _write_csv_file(self, lines):
        """
        Given a list of lines without newline characters, write them as is to a file. The lines are assumed to be
        CSV formatted from the server.
        :param lines: csv formatted lines without newline characters
        :return:
        """
        if not os.path.exists(self.destination_dir):
            os.mkdir(self.destination_dir)
        os.chdir(self.destination_dir)

        print('Writing party data to ' + self.destination_file)
        with open(self.destination_file, 'w', newline='') as file:
            for line in lines:
                file.write(line + "\n")


    def _get_active_parties(self):
        """
        Do the default query on the website and download the CSV data.
        :return: parsed array of CSV lines
        """
        self.driver.get(self.config["PARTY_FETCHER"]["base_url"])

        # Find the submit button and go to the results page
        submitBtn = self.driver.find_element_by_name("_ctl0:Content:btnSearch")
        submitBtn.click()

        # Find the CSV Download Button and select it
        csvBtn = self.driver.find_element_by_name("_ctl0:Content:ucExport:ibtnCSV")
        csvBtn.click()

        # Fetch the CSV Data and return the parsed array
        return self._parse_csv_string(self.driver.page_source)


    def _get_inactive_parties(self):
        """
        Select the Dissolved Status option and download the CSV data for the dissolved parties.
        :return: parsed array of CSV lines
        """
        self.driver.get(self.config["PARTY_FETCHER"]["base_url"])

        # Find the status select element and change it from Active to Dissolved.
        statusSelect = Select(self.driver.find_element_by_name("_ctl0:Content:ddlStatus"))
        statusSelect.select_by_visible_text('Dissolved')

        # Find the submit button and go to the results page
        submitBtn = self.driver.find_element_by_name("_ctl0:Content:btnSearch")
        submitBtn.click()

        # Find the CSV Download Button and select it
        csvBtn = self.driver.find_element_by_name("_ctl0:Content:ucExport:ibtnCSV")
        csvBtn.click()

        # Fetch the CSV Data and return the parsed array
        return self._parse_csv_string(self.driver.page_source)

    def _parse_csv_string(self, page_source):
        """
        Given a CSV file as a single string, split it into multiple lines and return it.
        :param page_source:
        :return:
        """
        return page_source.split('\r\n')


    def __del__(self):
        """
        Close down the web driver.
        :return:
        """
        self.driver.close()
        self.server.kill()


def main():
    fetcher = PartyFetcher("config.ini")
    fetcher.get_party_data()

if __name__ == "__main__":
    main()
