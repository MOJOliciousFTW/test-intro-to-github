import time
import logging


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
_LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":
    _LOGGER.debug("Starting")
    try:
        while True:
            _LOGGER.debug("beep")
            time.sleep(1)
    except KeyboardInterrupt:
        _LOGGER.debug("Stopped by keyboard interrupt.")
 
