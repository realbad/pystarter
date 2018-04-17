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
    nexturl = soup.find('a', attrs={'class': 'p1 nexe'}).get('href')
    return hreflist, nexturl


# 下载一周的所有壁纸
def downloadPic(ini_url):
    try:
        piclist = []
        html = getHTML(ini_url)
        soup = BeautifulSoup(html, 'html.parser')
        all_p = soup.find_all('img', attrs={'class': 'picact'})
        path = os.path.join(os.path.expanduser('~'), 'Downloads', 'ympic', soup.head.title.getText())
        try:
            next_url = soup.find('a', text='下一页').get('href')
            while True:
                for i in range(len(all_p)):
                    src = all_p[i].parent.get('href').split('?')[1]
                    piclist.append(src)
                    if not os.path.exists(path):
                        os.mkdir(path)
                        name = re.findall(r'/gamersky.*', piclist[i])[0]
                        with open(path + name, 'wb') as f:
                            pic = requests.get(piclist[i]).content
                            f.write(pic)
                    else:
                        name = re.findall(r'/gamersky.*', piclist[i])[0]
                        with open(path + name, 'wb') as f:
                            pic = requests.get(piclist[i]).content
                            f.write(pic)
                piclist.clear()
                # 下载一页进行调试
                # break
                if not next_url:
                    break
                url = next_url
                html = getHTML(url)
                soup = BeautifulSoup(html, 'html.parser')
                next_url = soup.find('a', text='下一页').get('href')
                all_p = soup.find_all('img', attrs={'class': 'picact'})
        except:
            pass
    except:
        return ''


def main():
    depth = 2
    ini_url = 'http://www.gamersky.com/ent/258/'
    html = getHTML(ini_url)
    hreflist, nexturl = parseHTML(html)
    # downloadPic(hreflist[0]) 测试代码
    for i in range(len(hreflist)):
        downloadPic(hreflist[i])
    # downloadPic(hreflist[0])
    for i in range(depth):
        url = ini_url + nexturl
        html = getHTML(url)
        hreflist, nexturl = parseHTML(html)
        for j in range(len(hreflist)):
            downloadPic(hreflist[j])


main()
