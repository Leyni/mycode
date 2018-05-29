# -*- coding: utf-8 -*-

import sys
import logging
import os
import string
import re
import time

err = None

debug_value = {}

# config
work_path = '/var/services/web/mycode/picture_recommend/'
log_path = work_path + '/log'
etc_path = work_path + '/etc'
data_path = '/var/services/photo/'
data_class = ['Furry', 'LoliTop', 'SecFurry', 'SecNormal', '东方同人', '其他', '初音', '动画', '同人', '游戏']

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/fetch.log',
    filemode = 'w')
# config end

for cls in data_class :
    file_list = [re.match(r'i(\d*) .*', x).group(1) for x in os.listdir(data_path + '/' + cls) if re.match(r'i\d* .*', x) != None]
    if file_list :
        print file_list[0]
