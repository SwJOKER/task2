# This is a sample Python script.
import time

from dirsync import sync
import logging
import sys
#папка донор
DIR_ONE = sys.argv[1]
#папка рецепиент
DIR_TWO = sys.argv[2]
#путь к логу
PATH_LOG = sys.argv[3]
#частота работы скрипта, сек
PERIOD = sys.argv[4]

def delete_garbage_log():
    f = open(PATH_LOG, 'r')
    lines = f.readlines()
    f.close()
    f = open(PATH_LOG, 'w')
    for line in lines:
        msg = line.split('|')[1]
        if (msg.find("Updating") != -1) or (msg.find("Copying") != -1) or (msg.find("Deleting") != -1) or (msg.find("created") != -1):
            f.write(line)
    f.close()

def syncronize_dir():
    file_log = logging.FileHandler(PATH_LOG)
    console_out = logging.StreamHandler()
    logging.basicConfig(handlers=(file_log, console_out),
                        format='[%(asctime)s | %(message)s',
                        datefmt='%m.%d.%Y %H:%M:%S',
                        level=logging.INFO)
    my_log = logging.getLogger('dir_syncronize')
    while True:
        sync(DIR_ONE, DIR_TWO, 'sync', purge=True, verbose=True, logger=my_log)
        delete_garbage_log()
        time.sleep(int(PERIOD))

if __name__ == '__main__':
    syncronize_dir()



