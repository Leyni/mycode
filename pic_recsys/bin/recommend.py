import urllib
import urllib2
import sys
import logging
import requests
import os
import string
import re
import time
import json
import MySQLdb
from contextlib import closing
from sgmllib import SGMLParser

err = None

debug_value = {}

# config
work_path = '/Users/kongfanyang/Develop/mycode/pic_recsys'
log_path = work_path + '/log'
etc_path = work_path + '/etc'
dat_path = work_path + '/dat'

rec_num = 1000

# config end

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/recommend.log',
    filemode = 'w')

class ProgressBar(object):

    def __init__(self, title,
                 count=0.0,
                 run_status=None,
                 fin_status=None,
                 total=100.0,
                 unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s]%s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.status)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # name status process unit split count unit
        _info = self.info % (self.title, self.status,
                             self.count/self.chunk_size, self.unit, self.seq, self.total/self.chunk_size, self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = '\r'
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        sys.stdout.write(self.__get_info() + end_str)
        sys.stdout.flush()


def downloadUrl(url, filename, timeout) :
    try :
        with closing(requests.get(url, stream=True, timeout = timeout)) as response :
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            progress = ProgressBar(url, total=content_size,
                unit="KB", chunk_size=chunk_size, run_status="Doing", fin_status="Done")
            with open(filename, "wb") as file :
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    progress.refresh(count=len(data))
        return response
    except Exception, err:
        logging.warning('download url = %s failed!' % url)
        raise Exception(err)


try:
    db = MySQLdb.connect("localhost", "leyni", "mina", "pic_rec", charset='utf8')
    cursor = db.cursor()

    sql = 'select count(1) from sample_e621_set where rec_status = 1'
    cursor.execute(sql)
    to_rec_num = rec_num - cursor.fetchone()[0]
    logging.info("need to recommend num = %d" % to_rec_num)

    sql = 'select pid, kw_lst, source_url from sample_e621_set where rec_status = 0 order by label desc limit %d' % to_rec_num
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        while True:
            try:
                pid = row[0]
                kw = json.loads(row[1])
                surl = row[2]
                file_ext = os.path.splitext(surl)[1]
                file_name = str(pid) + ' e621 ' + (' '.join(kw))[:128] + file_ext

                logging.info("remmand %d items, getting pid = %d, url = %s" % (to_rec_num, pid, surl))

                timeout = 60
                if (file_ext == '.swf' or file_ext == '.git') :
                    timeout = 300
                file_full_path = dat_path + '/recommend/' + file_name
                req = downloadUrl(url=surl, filename=file_full_path, timeout = timeout)
                if (req.status_code == 200) :
                    sql = "update sample_e621_set set rec_status = 1 where pid = %d" % pid
                    cursor.execute(sql)
                    break
                if (req.status_code == 404) :
                    sql = "update sample_e621_set set rec_status = 2, label_status = 4 where pid = %d" % pid
                    cursor.execute(sql)
                    os.remove(file_full_path)
                    break

            except Exception, err:
                pass
                #raise Exception(err)

        to_rec_num -= 1
        db.commit()
    db.close()
except Exception, err:
    raise Exception(err)

logging.info('------------recommend finish-----------')
