import re
import sys
import urllib.request
from utils.file_handler import read_websites_list
from utils.regex import find_expression_string
import certifi
import logging
import logging.config
from bs4 import BeautifulSoup

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

LOGGER = logging.getLogger(__name__)
PARSER = 'html.parser'
PHONE_REGEX = "\(\d{2}\)\d{5}-\d{4}|\(\d{2}\)\d{4}-\d{4}|\d{4} \d{3} \d{4}"

class Crawler:
    soup = None

    def __init__(self, url) -> None:
        self.url = url
        self.soup = BeautifulSoup(self.url, features=PARSER)

    def search_logo_page(self):
        """Get website content.
        Args:
            soup: website html content
        Returns:
            String: website logo path
        Raises: 
            Exception Generic Error
        """
        try:
            logo_alt = self.soup.find("img", {"alt": re.compile('logo', re.IGNORECASE)})
            if logo_alt:
                soup_logo = BeautifulSoup(str(logo_alt), features=PARSER)
                image = soup_logo.find("img")
                return image.get("src")
            logo_src = self.soup.find("img", {"src": re.compile('logo', re.IGNORECASE)})
            if logo_src:
                soup_logo = BeautifulSoup(str(logo_src), features=PARSER)
                image = soup_logo.find("img")
                return image.get("src")                
            LOGGER.info("No images were found :( in %s ", self.url)
            return ""
        except Exception as error:
            raise Exception
            LOGGER.error("An occured %s", error)
            sys.exit()

    def search_phone_numbers_page(self):
        """Get website content.
        Args:
            url: website url
        Returns:
            String: Website html
        Raises:
            Exception
        """
        try:
            phone_number = self.soup.findAll(text=re.compile(PHONE_REGEX, re.S))
            numbers = []
            for number in phone_number:
                numbers.append(re.search(PHONE_REGEX, str(number)).group())
            return numbers
        except Exception as error:
            raise Exception
            LOGGER.error("An occured %s", error)
            sys.exit()

    def _read_website_content(self, url):
        """Get website content.
        Args:
            url: website url
        Returns:
            String: Website html
        Raises:
            Exception
        """
        try:
            f = urllib.request.urlopen(url, cafile=certifi.where())
            data = f.read()
        except Exception as error:
            # LOGGER.error("Exception: {0}".format(error))
            f.close()
        else:
            return data.decode("utf8")
        finally:
            f.close()