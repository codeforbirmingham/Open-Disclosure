__author__ = 'cfilby'

import configparser
import sunlight


class SunlightFetcher:
    """
    Class responsible for fetching state specific Sunlight API Data.
    API Key is found in ~/.sunlight.key, Environment SUNLIGHT_API_KEY, or sunlight.config.api_key
    """

    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.state_code = self.config["SUNLIGHT"]["STATE_CODE"]

    def fetchData(self):
        federal_legislators = sunlight.congress.legislators(state=self.state_code)

        state_legislators = sunlight.openstates.legislators(state=self.state_code)
        state_bills = sunlight.openstates.bills(state='AL')
        state_districts = sunlight.openstates.districts(self.state_code.lower())
        state_committees = sunlight.openstates.committees(state=self.state_code)


def main():
    sunlightFetcher = SunlightFetcher('config.ini')
    sunlightFetcher.fetchData()

if __name__ == "__main__":
    main()