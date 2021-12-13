# This is a sample Python script.
import logging

import dirsync as ds
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dirsync import sync
import logging

def print_hi(name):
    file_log = logging.FileHandler('Log.log')
    console_out = logging.StreamHandler()

    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(levelname)s]: %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
    #logging.basicConfig(filename="sync.log", level=logging.DEBUG)
    my_log = logging.getLogger('dirsync')
    sync('./test1', './test2', 'sync', purge=True, verbose=True, logger=my_log)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
