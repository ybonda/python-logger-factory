from pathlib import Path
from logger_factory import LoggerFactory, LogLevel
import module1
import module2

LOG_DIR_PATH = Path(__file__).parent / 'logs'
LOG_FILE = "{}/{}.log".format(str(LOG_DIR_PATH), str(Path(__file__).stem))

log = LoggerFactory.get_logger(LOG_FILE, LogLevel.DEBUG)

def main():
    log.info("This is the main module!")
    module1.foo()
    module2.foo()
    
if __name__ == '__main__':
    main()