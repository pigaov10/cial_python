import sys
import logging
import logging.config

logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)

LOGGER = logging.getLogger(__name__)


def read_websites_list(file_path, mode="r"):
    """Return the websites urls."""
    try:
        f = open(file_path, mode)
    except FileNotFoundError:
        LOGGER.error("file not found in %s", file_path)
        sys.exit()
    except OSError as ioerror:
        LOGGER.error("I/O error occured %s", ioerror)
    else:
        return f.readlines()
    finally:
        f.close()
