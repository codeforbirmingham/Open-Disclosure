__author__ = 'cfilby'

import configparser, os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class PartyFetcher:
    """

    """

    def __init__(self, config_file):
        """

        :param config_file:
        :return:
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.destination_dir = self.config["PARTY_FETCHER"]["destination_dir"]
        self.destination_file = self.config["PARTY_FETCHER"]["destination_file"]
        self.driver = webdriver.Remote(
            command_executor= self.config["PARTY_FETCHER"]["selenium_server"],
            desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS
        )

    def get_party_data(self):
        """

        :return:
        """
        # Fetch the CSV Data
        active_parties = self.get_active_parties()
        inactive_parties = self.get_inactive_parties()

        # Remove the blank last row of both lists, remove the csv header row of inactive_parties and join the lists
        active_parties.pop()
        inactive_parties.pop(0)
        inactive_parties.pop()
        parties = active_parties + inactive_parties

        # Write the csv data
        self.write_csv_file(parties)



    def write_csv_file(self, lines):
        """

        :param lines:
        :return:
        """
        if not os.path.exists(self.destination_dir):
            os.mkdir(self.destination_dir)
        os.chdir(self.destination_dir)

        with open(self.destination_file, 'w', newline='') as file:
            for line in lines:
                file.write(line + "\n")




    def get_active_parties(self):
        """

        :return:
        """
        self.driver.get(self.config["PARTY_FETCHER"]["base_url"])

        submitBtn = self.driver.find_element_by_name("_ctl0:Content:btnSearch")
        submitBtn.click()

        csvBtn = self.driver.find_element_by_name("_ctl0:Content:ucExport:ibtnCSV")

        csvBtn.click()
        return self._parse_csv_string(self.driver.page_source)


    def get_inactive_parties(self):
        """

        :return:
        """
        self.driver.get(self.config["PARTY_FETCHER"]["base_url"])

        statusSelect = Select(self.driver.find_element_by_name("_ctl0:Content:ddlStatus"))
        statusSelect.select_by_visible_text('Dissolved')

        submitBtn = self.driver.find_element_by_name("_ctl0:Content:btnSearch")
        submitBtn.click()

        csvBtn = self.driver.find_element_by_name("_ctl0:Content:ucExport:ibtnCSV")
        csvBtn.click()

        return self._parse_csv_string(self.driver.page_source)

    def _parse_csv_string(self, page_source):
        """

        :param page_source:
        :return:
        """
        return page_source.split('\r\n')


    def close(self):
        """

        :return:
        """
        self.driver.close()



def main():
    fetcher = PartyFetcher("config.ini")
    fetcher.get_party_data()

if __name__ == "__main__":
    main()