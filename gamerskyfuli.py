from bs4 import BeautifulSoup
import requests
import re
import os
import time
import socket

socket.setdefaulttimeout(30)


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


# 获得一个Ajax中的所有标题url
def getpiclist(current_page):
    # ajax地址
    list_url = "http://db2.gamersky.com/LabelJsonpAjax.aspx"
    href_list = []
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    data = {
        'callback': 'jQuery1830174017864026059_1524115647541',
        # 此处jsondata的值不能是dict，否则服务器无法识别
        'jsondata': '{"type": "updatenodelabel", "isCache": true, "cacheTime": 60, "nodeId": "20119", "isNodeId": true,"page": %d}' % (
        current_page,),  # 根据当前页号修改数据
        '_': '1524116205248'
    }
    try:
        r = requests.get(url=list_url, params=data, headers=headers)
        # 此处param不是一个json类型的原因应该是request请求是一个get类型，data中的数据直接挂在url后面，而不是post提交类型
        html_text = r.content.decode("utf-8")
        # 很难说这是一个什么对象，可能是json，但使用jsonloads函数并不能对这个对象进行处理，只能手动提取
        json_list = eval(html_text[html_text.find("(") + 1:html_text.rfind(")")])
        # max_page = json_list['totalPages']
        body = json_list['body']
        soup = BeautifulSoup(body, 'html.parser')
        for tit in soup.find_all('div', attrs={'class': 'tit'}):
            href_list.append(tit.a.get('href'))
        return href_list
    except:
        return ''


# 下载一周的所有壁纸
def downloadPic(ini_url):
    try:
        piclist = []
        html = getHTML(ini_url)
        soup = BeautifulSoup(html, 'html.parser')
        all_p = soup.find_all('img', attrs={'class': 'picact'})
        path = os.path.join(os.path.expanduser('~'), 'Downloads', 'ympic', '福利', soup.head.title.getText())
    except:
        return ''
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
                        break
                    # 出现了命名不统一的情况
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
        try:
            html = getHTML(url)
            soup = BeautifulSoup(html, 'html.parser')
            next_url = soup.find('a', text='下一页').get('href')
        except:
            next_url = None
        all_p = soup.find_all('img', attrs={'class': 'picact'})



def main():
    ini_url = 'http://www.gamersky.com/ent/xz/'
    max_page = 60
    for current_page in range(max_page):
        print('\r正在爬取第{0}页\n'.format(current_page + 20), end='')
        href_list = getpiclist(current_page + 20)
        num = 1
        for href in href_list:
            downloadPic(href)
            print('\r{0}%'.format(num / len(href_list) * 100), end='')
            num += 1
        time.sleep(5)


if __name__ == '__main__':
    main()
