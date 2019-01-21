import requests
import json

def getJSON(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/'
                      '605.1.15 (KHTML, like Gecko) Version/11.1 Safari/605.1.15'}
    try:
        r = requests.get(url, timeout=10, headers=headers)
        r.raise_for_status()
        return r.content
    except:
        return ValueError

def main():
    url = "http://public-api.adsbexchange.com/VirtualRadar/AircraftList.json?"
    lat,lng,fDstL,fDstU = "40.068226","116.605530","0","100"
    # 距离经纬度，数据来源于实时雷达，非API，数据不准确
    addInfo = "lat=" + lat + "&lng=" + lng + "&fDstL=" + fDstL + "&fDstU=" + fDstU
    url = url + addInfo
    # print(url)
    r = getJSON(url)
    # print(r)
    j = json.loads(r)
    print(j)

main()