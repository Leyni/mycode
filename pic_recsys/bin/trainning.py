import sys
import logging
import json
from gensim.models import Word2Vec
import xgboost

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

class KW(object):
    def __iter__(self):
        err_cnt = 0
        err_pos_cnt = 0
        f = open(etc_path + '/query_result.tsv', 'r')
        l = f.readline()
        l = f.readline()
        while l:
            cols = l.strip().split('\t')
            label = cols[0]
            try:
                kws = json.loads(cols[1])
                yield kws
            except Exception, e:
                err_cnt += 1
                if cols[0] == 1: err_pos_cnt += 1
            l = f.readline()
        print err_cnt, err_pos_cnt

class Data(object):
    def __iter__(self):
        err_cnt = 0
        err_pos_cnt = 0
        cnt = 0
        f = open(etc_path + '/query_result.tsv', 'r')
        l = f.readline()
        l = f.readline()
        while l:
            cnt += 1
            if cnt % 1000 == 0 : print cnt
            cols = l.strip().split('\t')
            label = cols[0]
            try:
                kws = json.loads(cols[1])
                yield label, kws
            except Exception, e:
                err_cnt += 1
                if cols[0] == 1: err_pos_cnt += 1
            l = f.readline()
        print err_cnt, err_pos_cnt

def tranning_word2vec_model():
    kws = KW()
    model = Word2Vec(kws, size=1000, window = 10)
    model.save(etc_path + "/word_vec.model")

def item2vec():
    kws_vec = Data()
    out_file = open(etc_path + '/data_vec.txt', 'w')
    model = Word2Vec.load(etc_path + "/word_vec.model")
    for label, kws in kws_vec:
        item_vec = None
        for kw in kws:
            if item_vec is None:
                try:
                    item_vec = model[kw]
                except:
                    pass
            else:
                try:
                    item_vec += model[kw]
                except:
                    pass
        out_file.write('%s' % label)
        for i in range(len(item_vec)):
            out_file.write(' %d:%s' % (i, item_vec[i]))
        out_file.write('\n')

def train_classifier():
    dtrain = xgb.DMatrix('demo/data/agaricus.txt.train')
    dtest = xgb.DMatrix('demo/data/agaricus.txt.test')
    # specify parameters via map
    param = {'max_depth':2, 'eta':1, 'silent':0, 'objective':'binary:logistic' }
    num_round = 2
    bst = xgb.train(param, dtrain, num_round)
    # make prediction
    bst.save_model(etc_path + '/xgbt.model')

#tranning_word2vec_model()
item2vec()

# main

logging.info('------------tranning finish-----------')
