import urllib
import urllib2
import sys
import logging
import requests
import os
import string
import re
import time
from contextlib import closing
from sgmllib import SGMLParser

err = None

debug_value = {}

# config
work_path = '/var/services/web/mycode/picture_recommend/'
log_path = work_path + '/log'
etc_path = work_path + '/etc'

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + '/fetch.log',
    filemode = 'w')
# config end


class ListPageInfo(SGMLParser) :
    def __init__(self):
        SGMLParser.__init__(self)
        self.img_preview = []
        self.img_detail = []
        self.preview_cnt = 0
        self.comic_name = ''
        self.is_comic_name = 0
        self.is_pool = 0
        self.next_comic_url = ''
        # deal with download
        self.possible_img_src = ''
        self.img_tilte = ''
        self.is_tag = 0
        self.tags = []

    def start_img(self, attrs) :
        img_id = ''
        img_src = ''
        img_title = ''

        is_preview = 0
        for key, value in attrs :
            if key == 'class' and value[0:7] == 'preview' :
                self.preview_cnt = self.preview_cnt  + 1
                is_preview = 1
            if key == 'id' :
                img_id = value
            if key == 'src' :
                img_src = value
            if key == 'title' :
                img_title = value.split('\n')[0]
        if is_preview == 1:
            self.img_preview.append({'id' : img_id, 'src' : img_src, 'title' : img_title})

        is_detail = 0
        for key, value in attrs :
            if key == 'id' and value == 'image' :
                is_detail = 1
            if key == 'src' :
                img_src = value
            if key == 'alt' :
                img_title = value
        if is_detail == 1:
            self.img_title = img_title

    def start_param(self, attrs) :
        img_src = ''
        is_video = 0
        for key, value in attrs :
            if key == 'name' and value == 'movie' :
                is_video = 1
            if key == 'value' :
                img_src = value

        if is_video == 1:
            (filepath, tempfilename) = os.path.split(img_src);
            (shotname, extension) = os.path.splitext(tempfilename);
            self.img_title = shotname

    def start_source(self, attrs) :
        img_src = ''
        is_video = 0
        for key, value in attrs :
            if key == 'type' and value == 'video/webm' :
                is_video = 1
            if key == 'src' :
                img_src = value

        if is_video == 1:
            (filepath, tempfilename) = os.path.split(img_src);
            (shotname, extension) = os.path.splitext(tempfilename);
            self.img_title = shotname

    def start_a(self, attrs) :
        for key, value in attrs :
            if key == 'href' and re.match(r'/pool/show/\d+', value) != None :
                self.is_comic_name = 1
            if key == 'href' and re.match(r'/post/show/\d+', value) != None and self.is_pool == 2:
                self.next_comic_url = value
                #self.is_comic_name = 3
            if key == 'href' :
                self.possible_img_src = value
            if key == 'href' and re.match(r'/post/search\?tags=.*', value) != None :
                self.is_tag = 1

    def end_a(self) :
        if self.is_comic_name == 1 :
            self.is_comic_name = 0
        if self.is_tag == 1 :
            self.is_tag = 0

    def handle_data(self, data) :
        if self.is_comic_name == 1:
            self.comic_name += re.sub(r'[/]', '', data)
        if self.is_pool == 1 and '|' in data:
            self.is_pool = 2
        if data == 'Full Size' or (data == 'Download' and 'swf' in self.possible_img_src ):
            self.img_detail.append({'src' : self.possible_img_src, 'title' : self.img_title, 'tags' : self.tags})
        if self.is_tag == 1 :
            self.tags.append(data)

    def start_div(self, attrs) :
        for key, value in attrs :
            if key == 'class' and value == 'status-notice' :
                self.is_pool = 1

    def end_div(self):
        self.is_pool = 0


def getPageContent(url, host, ref_url) :
    try :
        logging.debug('get url = %s' % url)

        heads = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset':'utf-8;q=0.7,*;q=0.7',
            'Accept-Language':'en,zh;q=0.5',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Host':host,
            'Keep-Alive':'120',
            'Referer':ref_url,
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        opener.addheaders = heads.items()
        response = opener.open(req, timeout = 30)
        page = response.read()
        if (response.getcode() != 200) :
            raise Exception(err)
        return page
    except Exception, err:
        logging.warning('get url = %s failed!' % url)
        raise Exception(err)


def get_pid_from_file(file_name):
    with open(etc_path + '/' + file_name + '.process') as f :
        pid = f.readline()
    return pid


def save_pid_to_file(file_name, save_id):
    with open(etc_path + '/' + file_name + '.process', 'w') as code :
        code.write(save_id)


def get_pid_from_web(website):
    while (True) :
        try :
            url = 'https://' + website + '/post'
            list_page_content = getPageContent(url, website, 'https://' + website)
            break
        except Exception, err:
            logging.error('get current post url = %s failed!' % url)

    page_info = ListPageInfo()
    page_info.feed(list_page_content)
    pid = page_info.img_preview[0]['id'][1:]
    return pid


def paser_post_page(start_id):
    while (True) :
        try :
            url = 'https://e621.net/post?before_id=%s' % start_id
            list_page_content = getPageContent(url, 'e621.net', 'https://e621.net')
            break
        except Exception, err:
            logging.error('get url = %s failed!' % url)
            #raise Exception(err)
    page_info = ListPageInfo()
    page_info.feed(list_page_content)
    logging.debug('get %d/%d img from page url = %s ' % (len(page_info.img_preview), page_info.preview_cnt,  url))
    return page_info


def parse_detail_page(pid):
    url= 'https://e621.net/post/show/' + pid
    logging.debug('fetch id = %s, url = %s' % (pid, url))

    while (True) :
        try :
            detail_page_content = getPageContent(url, 'e621.net', 'https://e621.net/')
            break
        except Exception, err:
            logging.error('get url = %s failed!' % url)
            time.sleep(1)
            # TODO
            raise Exception(err)

    detail_info = ListPageInfo()
    detail_info.feed(detail_page_content)
    return detail_info


# main
if len(sys.argv) == 1 :
    start_id = get_pid_from_web('e621.net')
    end_id = get_pid_from_file('fetch')
    logging.info('get start img id = %s end img id = %s' % (start_id, end_id))
else :
    start_id = sys.argv[1]
    end_id = sys.argv[2]

save_id = start_id
while (string.atoi(start_id) > string.atoi(end_id)):
    # parse list page
    page_info = paser_post_page(start_id)

    if (len(page_info.img_preview) == 0) :
        start_id = str(string.atoi(start_id) - 50)
        continue

    for item in page_info.img_preview :
        if (string.atoi(start_id) < string.atoi(end_id)) :
            break
        while (True) :
            try:
                # get source image info
                file_ext = os.path.splitext(item['src'])[1]
                img_id = item['id'][1:]

                if file_ext not in ['.png', '.jpg', '.gif', '.swf', '.webm']:
                    break

                detail_info = parse_detail_page(img_id)

                for detail_item in detail_info.img_detail :
                    try:
                        print 'e621', img_id, file_ext, item['src'], detail_item['src'], detail_item['tags']
                        logging.debug('fetch %s' % (item['id']))
                        break
                    except Exception, err:
                        logging.error('insert img_id= %s failed!' % img_id)
                        raise Exception(err)

                start_id = img_id
                logging.debug('current start_id = %s' % start_id)

                break
            except Exception, err:
                logging.error('get url = %s failed!' % item['src'])
                # TODO
                raise Exception(err)

save_pid_to_file('fetch', save_id)
logging.info('------------fetch finish-----------')
