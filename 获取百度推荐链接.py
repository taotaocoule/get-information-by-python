import urllib2
import urllib
from bs4 import BeautifulSoup
a=raw_input('ÊäÈëËÑË÷´Ê')
b='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd='
c=a.decode('gb2312').encode('utf-8')
d=urllib2.quote(c)
e=b+d
res=urllib.urlopen(e)
red=res.read()
soup=BeautifulSoup(red)
print soup.find_all('th')
