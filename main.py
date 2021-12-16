import time
from dirsync import sync
import logging
from logging import LogRecord
import sys

#папка донор
DIR_ONE = sys.argv[1]
#папка рецепиент
DIR_TWO = sys.argv[2]
#путь к логу
PATH_LOG = sys.argv[3]
#частота работы скрипта, сек
PERIOD = sys.argv[4]

def filter_log(record: LogRecord) -> bool:
    if (record.getMessage().find("Updating") != -1) or (record.getMessage().find("Copying") != -1)\
            or (record.getMessage().find("Deleting") != -1) or (record.getMessage().find("created") != -1):
        return True
    return False


def syncronize_dir():
    file_log = logging.FileHandler(PATH_LOG)
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
    my_log = logging.getLogger('dir_syncronize')
    my_log.addFilter(filter_log)
    while True:
        sync(DIR_ONE, DIR_TWO, 'sync', purge=True, verbose=True, logger=my_log)
        time.sleep(int(PERIOD))

if __name__ == '__main__':
    syncronize_dir()



