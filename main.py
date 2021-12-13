# This is a sample Python script.
import logging

import dirsync as ds
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from dirsync import sync
import logging

def print_hi(name):
    logging.basicConfig(filename="sync.log", level=logging.DEBUG)
    my_log = logging.getLogger('dirsync')
    sync('./test1', './test2', 'sync', purge=True, verbose=True, logger=my_log)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
