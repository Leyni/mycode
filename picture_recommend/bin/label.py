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
data_class = ['Furry', 'LoliTop', 'SecFurry', 'SecNormal', '东方同人', '其他', '其他/SecFurryGif', '其他/SecNormalGif', \
        '其他/SecSwfWebm', '初音', '动画', '同人', '游戏']
res_path = '/usr/local/debian-chroot/var/chroottarget/home/mycode/picture_recommend/etc/'

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/fetch.log',
    filemode = 'w')
# config end

def listdir(path, fileList):  #传入存储的list
    for file in os.listdir(path):
	file_path = os.path.join(path, file)
	if os.path.isdir(file_path) and '@' not in file_path:
            print file_path
            listdir(file_path, fileList)
	else:
            pat = re.match(r'i(\d*) .*', file)
            if pat != None:
                fileList.append(pat.group(1))

command = sys.argv[1]
if command == 'fetch':
    fileList = []
    listdir(data_path, fileList)
    with open(res_path + '/label_id_list.txt', 'a') as code :
        for x in fileList:
            code.write(x + '\n')
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
