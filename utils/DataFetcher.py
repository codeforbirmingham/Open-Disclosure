
import configparser, datetime, os, urllib.request, zipfile

class DataFetcher:
    """
    DataFetcher Object Responsible for downloading and extracting the Extract Files from the alabamavotes.gov website
    """

    def __init__(self, config_file, year=datetime.date.today().year):
        """
        Create a new DataFetcher object. Uses the provided config file to load the base URL for the request and to read
        the base file names that can all be downloaded from that URL. These base_file names are then prepended with
        the specified or current year to create the full file download name.
        :param config_file:
        :return:
        """
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.destination_dir = self.config["DATA_FETCHER"]["destination_dir"]
        self.chunk_size = int(self.config["DATA_FETCHER"]["chunk_size"])
        self.base_url = self.config["DATA_FETCHER"]["base_url"]
        self.year = str(year)
        self.files = [ '_'.join([self.year, file_name]) for file_name in self.config["DATA_FETCHER"]["file_names"].split(',')]


    def fetch_files(self):
        """
        Download and extract all of the files into the destination directory specified by the config and year
        :return:
        """
        if not os.path.exists(self.destination_dir):
            os.mkdir(self.destination_dir)

        os.chdir(self.destination_dir)

        for file in self.files:
            file_url = ''.join([self.base_url, file])
            if self._download_file(file, file_url):
                self._extract_file(file)
            print()

    def _download_file(self, file_name, file_url):
        """
        Given a file_name and file_url, download the file specified at file_url and save it into file. Returns whether or not
        the operation was successful.
        :param file_name: name of the file to open and write bytestream into
        :param file_url: web url to fetch the file contents from
        :return: True if the download was successful, false if an HTTPError occurs
        """
        try:
            response = urllib.request.urlopen(file_url)
            file_size = int(response.getheader('Content-Length').strip())
            bytes_downloaded = 0

            with open(file_name, "wb") as f:
                print('Downloading: ' + file_url)
                while True:
                    chunk = response.read(self.chunk_size)
                    bytes_downloaded += len(chunk)

                    if not chunk:
                        break

                    f.write(chunk)
        except urllib.error.HTTPError as err:
            print('Unable to download file at' + file_url + ': '+ str(err))
            return False

        return True

    def _extract_file(self, file_name):
        """
        Extract the contents of the specified file into the current directory and remove the old file if the extract is
        successful.
        :param file_name: Name/Path of the file to extract
        :return: True if the extract is successful, False otherwise.
        """
        try:
            print("Extracting file into " + file_name + "...", end="")
            zipFile = zipfile.ZipFile(file_name)
            zipFile.extractall()
        except zipfile.BadZipfile as e:
            print("Bad zipfile provided: ", e, zipFile)
            return False
        except zipfile.LargeZipFile as e:
            print("Zipfile too large: ", e, zipFile)
            return False
        print("done!")

        os.remove(file_name)
        return True


def main():
    fetcher = DataFetcher("config.ini")
    fetcher.fetch_files()

if __name__ == "__main__":
    main()