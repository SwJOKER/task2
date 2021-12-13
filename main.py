# This is a sample Python script.
import logging
import time

import dirsync as ds
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dirsync import sync
import logging
import sys
DIR_ONE = sys.argv[1]
DIR_TWO = sys.argv[2]
PATH_LOG = sys.argv[3]
PERIOD = sys.argv[4]

def syncronize_dir():
    file_log = logging.FileHandler(PATH_LOG)
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
    my_log = logging.getLogger('dir_syncronize')
    while True:
        sync(DIR_ONE, DIR_TWO, 'sync', purge=True, verbose=True, logger=my_log)
        time.sleep(int(PERIOD))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    syncronize_dir()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
