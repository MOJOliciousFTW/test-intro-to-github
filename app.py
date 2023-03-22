import time
import logging
import os


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

_LOGGER.debug(os.environ.get("STAGE") or "local")

if __name__ == "__main__":
    _LOGGER.debug("Starting")
    try:
        while True:
            _LOGGER.debug("beep")
            time.sleep(1)
    except KeyboardInterrupt:
        _LOGGER.debug("Stopped by keyboard interrupt.")
 
