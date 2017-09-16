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

#root_path = '/var/services/homes/leyni/CloudStation/Drive/Entertain/Picture'
root_path = './'
log_path = './'

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

    def start_img(self, attrs) :
        img_id = ''
        img_src = ''
        img_title = ''

        is_preview = 0
        for key, value in attrs :
            if key == 'class' and value[0:7] == 'preview' :
                self.preview_cnt = self.preview_cnt  + 1
                is_preview = 1
            if key == 'alt' :
                img_id = value[6:].strip()
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
            self.img_detail.append({'src' : img_src, 'title' : img_title})

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
            self.img_detail.append({'src' : img_src, 'title' : shotname})

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
            self.img_detail.append({'src' : img_src, 'title' : shotname})

    def start_a(self, attrs) :
        for key, value in attrs :
            if key == 'href' and re.match(r'/pool/show/\d+', value) != None :
                self.is_comic_name = 1
            if key == 'href' and re.match(r'/post/show/\d+', value) != None and self.is_pool == 2:
                self.next_comic_url = value
                #self.is_comic_name = 3

    def end_a(self) :
        if self.is_comic_name == 1 :
            self.is_comic_name = 0

    def handle_data(self, data) :
        if self.is_comic_name == 1:
            self.comic_name += re.sub(r'[/]', '', data)
        if self.is_pool == 1 and '|' in data:
            self.is_pool = 2

    def start_div(self, attrs) :
        for key, value in attrs :
            if key == 'class' and value == 'status-notice' :
                self.is_pool = 1

    def end_div(self):
        self.is_pool = 0


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
            'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        opener.addheaders = heads.items()
        page = opener.open(req, timeout = 30).read()
        return page
    except Exception, err:
        logging.warning('get url = %s failed!' % url)
        raise Exception(err)


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


# main
command = sys.argv[1]

logging.basicConfig(level = logging.DEBUG,
    format = '%(asctime)s [line:%(lineno)d] %(levelname)s %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    filename = log_path + 'e621_' + command + '.log',
    filemode = 'w')

# argv1 preview = get preview; download = download source file
# argv2 start image id
# argv3 end-limit image id

if (command == 'preview') :
    if len(sys.argv) == 2 :
        with open(log_path + 'process.dat') as f :
            end_id = f.readline()

        while (True) :
            try :
                url = 'http://www.youhate.us/index.php?page=post&s=list&tags=all&pid=0'
                list_page_content = getPageContent(url, 'youhate.us', 'https://www.youhate.us')
                break
            except Exception, err:
                logging.error('get url = %s failed!' % url)

        page_info = ListPageInfo()
        page_info.feed(list_page_content)
        start_id = page_info.img_preview[0]['id']
        logging.info('get start img id = %s end img id = %s' % (start_id, end_id))
    else :
        start_id = sys.argv[2]
        end_id = sys.argv[3]

    pid = string.atoi(start_id) - string.atoi(end_id) + 1

    save_id = start_id

    point_id = 0
    print [start_id, end_id, point_id, pid]
    while (point_id <= pid):
        # parse list page
        while (True) :
            try :
                url = 'http://www.youhate.us/index.php?page=post&s=list&tags=all&pid=%s' % point_id
                list_page_content = getPageContent(url, 'youhate.us', 'https://www.youhate.us')
                break
            except Exception, err:
                logging.error('get url = %s failed!' % url)
                #raise Exception(err)

        page_info = ListPageInfo()
        page_info.feed(list_page_content)
        logging.debug('get %d/%d img from page url = %s ' % (len(page_info.img_preview), page_info.preview_cnt,  url))

        # download preview image

        for item in page_info.img_preview :
            while (True) :
                try:
                    file_ext = os.path.splitext(item['src'])[1]
                    file_name = item['id'] + file_ext

                    logging.debug('download %s' % (file_name))

                    req = requests.get('https:' + item['src'], timeout = 10)
                    with open(root_path + 'g_preview/' + file_name, 'wb') as code :
                        code.write(req.content)

                    start_id = item['id']

                    logging.debug('current start_id = %s' % start_id)
                    break
                except Exception, err:
                    logging.error('get url = %s failed!' % item['src'])
                    #raise Exception(err)

            if (string.atoi(start_id) < string.atoi(end_id)) :
                break

        point_id = point_id + 42

    with open(log_path + 'process.dat', 'w') as code :
        code.write(save_id)
    logging.info('------------preview finish-----------')

if (command == 'download') :
    logging.info('------------download start-----------')

    #get perview image info
    files = os.listdir(root_path + 'g_done')
    files_cnt = len(files)
    cnt = 0
    for file in files:
        cnt = cnt + 1
        file_name = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]

        sys.stdout.write('process %d/%d %s\n' % (cnt, files_cnt, file_name))

        if (file_ext == '.png' or file_ext == '.jpg' or file_ext == '.gif' or file_ext == '.swf' or file_ext == '.webm') :

            url = 'https://gelbooru.com/index.php?page=post&s=view&id=' + file_name
            logging.debug('download id = %s, url = %s' % (file_name, url))

            while (True) :
                try :
                    detail_page_content = getPageContent(url, 'gelbooru', 'https://www.gelbooru.com')
                    break
                except Exception, err:
                    logging.error('get url = %s failed!' % url)
                    time.sleep(1)
                    #raise Exception(err)

            detail_info = ListPageInfo()
            detail_info.feed(detail_page_content)

            img_id = file_name
            for item in detail_info.img_detail :
                while (True) :
                    try:
                        if not os.path.isfile(root_path + 'g_done/' + file) :
                            break
                        file_ext = os.path.splitext(item['src'])[1]
                        file_name = img_id + ' ' + re.sub(r'[^a-zA-Z0-9_ ]', '', item['title'])[:128] + file_ext

                        logging.debug('download %s' % (file_name))

                        timeout = 60
                        if (file_ext == '.swf' or file_ext == '.git') :
                            timeout = 300

                        req = downloadUrl(url='https://gelbooru.com' + item['src'], filename=root_path + 'source/' + file_name, timeout = timeout)
                        #req = requests.get(item['src'], timeout = timeout)
                        if (req.status_code == 200) :
                        #    with open(root_path + 'source/' + file_name, 'wb') as code :
                        #        code.write(req.content)
                            os.remove(root_path + 'g_done/' + file)
                            break
                    except Exception, err:
                        logging.error('get url = %s failed!' % item['src'])
                        time.sleep(1)
                        #raise Exception(err)

    logging.info('------------download finish-----------')

if (command == 'comic') :
    logging.info('------------comic start-----------')
    start_id = sys.argv[2]

    # parse list page
    url = 'https://e621.net/post/show/%s' % start_id
    page_cnt = 1
    while (url != '') :
        try :
            page_content = getPageContent(url, 'e621.net', 'https://e621.net')

            page_info = ListPageInfo()
            page_info.feed(page_content)

            save_path = root_path + 'source/' + page_info.comic_name
            if not os.path.isdir(save_path) :
                logging.info('get comic name = %s' % (page_info.comic_name))
                os.mkdir(save_path)

            file_name = str(page_cnt).zfill(3)
            for item in page_info.img_detail :
                while (True) :
                    try:
                        file_ext = os.path.splitext(item['src'])[1]
                        file_name = str(page_cnt).zfill(3) + file_ext

                        logging.debug('download %s' % (file_name))

                        timeout = 60
                        if (file_ext == '.swf' or file_ext == '.git') :
                            timeout = 300
                        req = requests.get(item['src'], timeout = timeout)
                        if (req.status_code == 200) :
                            with open(save_path + '/' + file_name, 'wb') as code :
                                code.write(req.content)
                            break
                    except Exception, err:
                        logging.error('get url = %s failed!' % item['src'])
                        time.sleep(1)
                        #raise Exception(err)

            if page_info.next_comic_url != '' :
                url = 'https://e621.net' + page_info.next_comic_url
            else :
                url = ''

            page_cnt += 1
        except Exception, err:
            logging.error('get url = %s failed!' % url)
            #raise Exception(err)

    logging.info('------------comic finish-----------')
