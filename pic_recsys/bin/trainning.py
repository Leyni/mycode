import sys
import logging
import json
import MySQLdb
from gensim.models import Word2Vec

err = None

debug_value = {}

# config
work_path = '/Users/kongfanyang/Develop/mycode/pic_recsys'
log_path = work_path + '/log'
etc_path = work_path + '/etc'
# config end

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/trainning.log',
    filemode = 'w')

def get_kw_gen():
    db = MySQLdb.connect("localhost", "leyni", "mina", "pic_rec", charset='utf8')
    cursor = db.cursor()

    sql = 'select kw_lst from sample_e621_set where label_status = 1'
    cursor.execute(sql)

    col = cursor.fetchone()
    while col:
        kws = json.loads(col[0].encode('utf8'))
        yield kws

    db.close()

# main
try:
     model = Word2Vec(get_kw_gen(), size=1000, window = 10)
     model.save(etc_path + "/word_vec.model")
except Exception, err:
    raise Exception(err)

logging.info('------------tranning finish-----------')
