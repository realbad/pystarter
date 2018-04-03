import re
p = re.compile('P(Y|YT|YTH|YTHO?N)')
t = re.compile('PY[^PY]{0,10}')
print(p,t)