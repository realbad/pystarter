import requests
from bs4 import BeautifulSoup
import os
import re


# 爬取游民星空壁纸，深度为depth

def getHTML(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'}
    try:
        r = requests.get(url, timeout=10, headers=headers)
        r.raise_for_status()
        return r.content
    except:
        return ValueError


# 页面中几周的list和下一页的url
def parseHTML(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find_all('ul', 'pictxt')[0]
    li = ul.find_all('li')
    hreflist = []
    for i in range(len(li)):
        href = li[i].find_all('div', attrs={'class': 'tit'})[0].a.get('href')
        hreflist.append(href)
    try:
        nexturl = soup.find('a', attrs={'class': 'p1 nexe'}).get('href')
    except:
        nexturl = None

    return hreflist, nexturl


# 下载一周的所有壁纸
def downloadPic(ini_url):
    piclist = []
    html = getHTML(ini_url)
    soup = BeautifulSoup(html, 'html.parser')
    all_p = soup.find_all('img', attrs={'class': 'picact'})
    path = os.path.join(os.path.expanduser('~'), 'Downloads', 'ympic', '壁纸',soup.head.title.getText())
    try:
        next_url = soup.find('a', text='下一页').get('href')
    except:
        next_url = None
    while True:
        for i in range(len(all_p)):
            try:
                src = all_p[i].parent.get('href').split('?')[1]
                piclist.append(src)
            except:
                pass
            if not os.path.exists(path):
                try:
                    os.mkdir(path)
                except:
                    pass
                try:
                    name = re.findall(r'/gamersky.*', piclist[i])[0]
                except:
                    try:
                        name = re.findall(r'/image0.*', piclist[i])[0]
                    except:
                        pass
                if not os.path.isfile(path + name):
                    with open(path + name, 'wb') as f:
                        pic = requests.get(piclist[i]).content
                        f.write(pic)
                else:
                    pass
            else:
                try:
                    name = re.findall(r'/gamersky.*', piclist[i])[0]
                except:
                    try:
                        name = re.findall(r'/image0.*', piclist[i])[0]
                    except:
                        break
                if not os.path.isfile(path + name):
                    with open(path + name, 'wb') as f:
                        pic = requests.get(piclist[i]).content
                        f.write(pic)
                else:
                    pass
        piclist.clear()
        # 下载一页进行调试
        # break
        if not next_url:
            break
        url = next_url
        html = getHTML(url)
        soup = BeautifulSoup(html, 'html.parser')
        try:
            next_url = soup.find('a', text='下一页').get('href')
        except:
            next_url = None
        all_p = soup.find_all('img', attrs={'class': 'picact'})


def main():
    depth = 2
    ini_url = 'http://www.gamersky.com/ent/258/'
    html = getHTML(ini_url)
    hreflist, nexturl = parseHTML(html)
    # downloadPic(hreflist[0]) 测试代码
    for i in range(len(hreflist)):
        downloadPic(hreflist[i])
    #
    for i in range(depth - 1):
        print('\r正在爬取第{0}页\n'.format(i+1), end='')
        url = ini_url + nexturl
        html = getHTML(url)
        hreflist, nexturl = parseHTML(html)
        num = 1
        for j in range(len(hreflist)):
            downloadPic(hreflist[j])
            print('\r{0}%'.format(num/len(hreflist) * 100), end='')
            num += 1


main()
# downloadPic('http://www.gamersky.com/ent/201505/590204.shtml')