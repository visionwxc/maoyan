from urllib import request
from urllib import parse
import json
import regex as re
import os

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent', user_agent}
params = 'q&viewFlag=A&sortType=default&searchStyle=&searchRegion=city%3A&searchFansNum=&currentPage=1&pageSize=100'


def getHome():
    url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
    req = request.Request(url)
    req.add_header('User-Agent', user_agent)
    html = request.urlopen(req, parse.quote_plus(params).encode(encoding='UTF-8'))
    res = html.read().decode('gbk').encode('utf-8')
    data = json.loads(res)
    for item in data['data']['searchDOList']:
        getInfo(item['userId'], item['realName'])


def getInfo(userId, realName):
    url = 'https://mm.taobao.com/self/aiShow.htm?userId=' + str(userId)
    req = request.Request(url)
    html = request.urlopen(req).read().decode('gbk').encode('utf-8')

    pattern = re.compile('<img.*?src=(.*?)/>', re.S)
    items = re.findall(pattern, html)
    x = 0
    for item in items:
        if re.match(r'.*(.jpg")$', item.strip()):
            tt = 'http:' + re.split('"', item.strip())[1]
            down_image(tt, x, realName)
            x = x + 1
    print('下载完毕')


def down_image(url, filename, realName):
    req = request.Request(url=url)
    folder = 'D:\\images\\%s' % realName
    if os.path.isdir(folder):
        pass
    else:
        os.makedirs(folder)

    f = folder + '\\%s.jpg' % filename
    if not os.path.isfile(f):
        print(f)
        binary_data = request.urlopen(req).read()
        with open(f, 'wb') as temp_file:
            temp_file.write(binary_data)


if __name__ == '__main__':
    getHome()
