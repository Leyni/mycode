# -*- coding: utf-8 -*-

import sys
import logging
import os
import string
import re
import time
import MySQLdb

err = None

debug_value = {}

# config
#work_path = '/var/services/web/mycode/picture_recommend/'
work_path = '/home/mycode/picture_recommend/'
log_path = work_path + '/log'
etc_path = work_path + '/etc'
data_path = '/var/services/photo/'
data_class = ['Furry', 'LoliTop', 'SecFurry', 'SecNormal', '东方同人', '其他', '初音', '动画', '同人', '游戏']
res_path = '/usr/local/debian-chroot/var/chroottarget/home/mycode/picture_recommend/etc/'

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/fetch.log',
    filemode = 'w')
# config end


command = sys.argv[1]
if command == 'fetch':
    with open(res_path + '/label_id_list.txt', 'a') as code :
        for cls in data_class :
            for x in os.listdir(data_path + '/' + cls):
                pat = re.match(r'i(\d*) .*', x)
                if pat != None:
                    code.write(pat.group(1) + '\n')
    code.close()

if command == 'flush':
    db = MySQLdb.connect("localhost", "leyni", "mina", "pic_rec", charset='utf8')
    cursor = db.cursor()

    with open(etc_path + '/label_id_list.txt', 'r') as f:
        for l in f.readlines():
            sql = "update pic_rec.sample_set set label = 1, label_status = 1 where pid = '%s'" % l.strip()
            cursor.execute(sql)

    db.commit()
    db.close()
