# -*- coding: utf-8 -*-

import sys
import logging
import os
import string
import re
import time
import MySQLdb
import shutil

err = None

debug_value = {}

# config
work_path = '/Users/kongfanyang/Develop/mycode/pic_recsys'
log_path = work_path + '/log'
etc_path = work_path + '/etc'
dat_path = work_path + '/dat'
target_path = '/Users/kongfanyang/CloudStation/Entertain/Picture/source'
pos_dirs = ['Anime', 'Doujin', 'Furry', 'Game', 'Miku', 'SecFurry', 'SecNormal', 'SecSwfWebm', 'Touhou']
neg_dirs = ['delete']

# config end

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/fetch.log',
    filemode = 'w')

try:
    db = MySQLdb.connect("localhost", "leyni", "mina", "pic_rec", charset='utf8')
    cursor = db.cursor()

    for d in pos_dirs:
        for file_name in os.listdir(dat_path + '/' + d):
            pat = re.match(r'(\d*?) .*', file_name)
            if pat != None:
                pid = pat.group(1)
                sql = 'update sample_e621_set set rec_status = 2, label = 1, label_status = 1 where pid = %d' % int(pid)
                cursor.execute(sql)
                shutil.move(dat_path + '/' + d + '/' + file_name, target_path + '/' + d)
        db.commit()

    for d in neg_dirs:
        for file_name in os.listdir(dat_path + '/' + d):
            pat = re.match(r'(\d*?) .*', file_name)
            if pat != None:
                pid = pat.group(1)
                sql = 'update sample_e621_set set rec_status = 2, label = 0, label_status = 1 where pid = %d' % int(pid)
                cursor.execute(sql)
                os.remove(dat_path + '/' + d + '/' + file_name)
        db.commit()

    db.close()

except Exception, err:
    raise Exception(err)

logging.info('------------sync finish-----------')
