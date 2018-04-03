import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        # print("Error")
        return ""


def fillUnivList(html, ulist):
    soup = BeautifulSoup(html, "html.parser")
    i = 0
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            i = i + 1
            ulist.append([i, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}"
    print(tplt.format("排名", "学校", "地点", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))
    print("Suc" + str(num))


def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(html, uinfo)
    printUnivList(uinfo, 20)


if __name__ == '__main__':
    main()
