from bs4 import BeautifulSoup
import requests
import re  # 正则表达式库re

url = "http://python123.io/ws/demo.html"
r = requests.get(url, timeout=300)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

for link in soup.find_all('a'):  # 寻找所有a标签的内容
    print(link.get('href'))  # a标签中的所有url链接

# 利用正则表达式打印出所有标签名字中含有b的标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

# 找到p中所有属性为course的内容,返回一个list类型，find返回字符串
print(soup.find_all('p', 'course'))

# 找到所有属性中带有id = link字样的信息，不用正则表达式需要准确给出
print(soup.find_all(id=re.compile('link')))

print(soup.find_all(string=re.compile('python')), soup.find_all(string='Python'),
      soup.find_all(string=re.compile('Python')))

# soup(...) 等价于 soup.find_all(...)
#<tag>(...) 等价于 <tag>(...)
print(soup(string = 'Basic Python'))

