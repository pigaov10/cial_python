import grequests
import logging
import logging.config
from utils.file_handler import read_websites_list
from utils.crawler import Crawler
from models.website_page import WebSitePage
logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

LOGGER = logging.getLogger(__name__)

def main():
    try:
        websites = read_websites_list("input/websites.txt")
        requests = (grequests.get(row) for row in websites)
        threaded = grequests.imap(requests, grequests.Pool(10))
        response = []
        for website in threaded:
            crawler = Crawler(website.text)
            logo = crawler.search_logo_page()
            phone_numbers = crawler.search_phone_numbers_page()
            models = WebSitePage(logo, phone_numbers)
            response.append(models.__dict__)
        LOGGER.info(response)
    except UnboundLocalError as e:
        LOGGER.error(e)


if __name__=="__main__":
    main()
