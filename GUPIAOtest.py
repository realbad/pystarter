import requests
import re
from bs4 import BeautifulSoup
import traceback


def getHTMLText(url, code = 'utf-8'):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()
        r.encoding = code
        # r.encoding = r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return ""


def getStockList(lst, url):
    html = getHTMLText(url, 'GB2312')
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz][6,9,0,1,3]\d{5}", href)[0])
        except:
            # traceback.print_exc()
            continue
    # print(len(lst))
    # with open('lst.txt', 'a', encoding= 'utf-8') as f:
    #     f.write(str(lst))



def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value

            with open(fpath, 'a', encoding='utf-8') as f:
                for (k,v) in infoDict.items():
                    f.write(k.strip())
                    f.write(':')
                    f.write(v.strip())
                    f.write(' ')
                f.write('\n')
                # f.write(str(infoDict) + '\n')
                count = count + 1
                print('\rprocessing:{:.2f}%'.format(count*100/len(lst)), end = '')
        except:
            # traceback.print_exc()
            count = count + 1
            print('\rprocessing:{:.2f}%'.format(count * 100 / len(lst)), end='')
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)

if __name__ == '__main__':
    main()