import logging
import logging.config

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

LOGGER = logging.getLogger(__name__)

class WebSitePage:
    def __init__(self, logo="", phone_numbers=[]):
        self.phone_numbers = phone_numbers
        self.logo = logo

    @property
    def phone_numbers(self):
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        if not isinstance(phone_numbers, list) or not phone_numbers:
            LOGGER.error("Phone numbers is required or not empty")
        self._phone_numbers = phone_numbers

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, logo):
        if not isinstance(logo, str):
            LOGGER.error("Logo must be a string")
        self._logo = logo