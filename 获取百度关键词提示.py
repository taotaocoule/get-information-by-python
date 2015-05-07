import urllib2
import urllib
import re
word=raw_input(" ‰»Îπÿº¸¥ ")
a='http://suggestion.baidu.com/su?wd='
b='&json=1&p=3&sid=13457_1456_12657_13074_12824_10812_12867_13321_13691_10562_12723_13761_13256_13780_11702_13838_13085_8498&req=2&bs=%E7%BD%91%E7%9B%9F%E6%8E%A8%E5%B9%BF%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D&pbs=%E7%BD%91%E7%9B%9F%E6%8E%A8%E5%B9%BF%E6%98%AF%E4%BB%80%E4%B9%88%E6%84%8F%E6%80%9D&cb=jQuery110208002315869089216_1430977396213&_=1430977396250'
c=word.decode('gb2312').encode('utf-8')
d=urllib2.quote(c)
u=a+d+b
m=urllib.urlopen(u)
n=m.read()
z=n.split(':')
s=len(z)-1
o=z[s]
r=o.split('","')
soo=r[0]
r[0]=soo[2:]
suo=r[len(r)-1]
r[len(r)-1]=suo[:-5]
for i in range(len(r)):
    print r[i]
    
 
    

    
