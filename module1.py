from pathlib import Path
from logger_factory import LoggerFactory, LogLevel

LOG_DIR_PATH = Path(__file__).parent / 'logs'
LOG_FILE = "{}/{}.log".format(str(LOG_DIR_PATH), str(Path(__file__).stem))
    
log = LoggerFactory.get_logger(LOG_FILE, LogLevel.DEBUG)


def foo():
    log.info("This is module1!")
    log.debug("CodeFlex.co - All about Software Development & DevOps")
    log.warning("CodeFlex.co - All about Software Development & DevOps")
    log.error("CodeFlex.co - All about Software Development & DevOps")
