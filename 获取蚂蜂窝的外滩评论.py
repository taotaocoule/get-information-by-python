import urllib2
import re
road=raw_input('请输入路径和文件名')
b=r'http://www.mafengwo.cn/qa/ajax_pager.php?kw=%E5%A4%96%E6%BB%A9&sort=0&action=question_search&start='
c=range(10,380,10)
d=range(37)
e=re.compile(r'data-title=\\"([^"]+)\\"')
m=re.compile(r'class="_j_filter_click" target="_blank"\\u003e([^"]+)\\u003c\\/a\\u003e\n')
n=re.compile(r'\\u003cdiv class="desc"\\u003e\\u003cp\\u003e([^"]+)\\u003c\\/p\\u003e\\u003c\\/div\\u003e\n')
for i in d:
    u=b+str(c[i])
    r=urllib2.urlopen(u)
    res=r.read()
    h=e.findall(res)
    f=open(road,'a')
    for j in range(len(h)):
        f.write(h[j].decode('unicode-escape',"ignore").encode('utf-8'))
        f.write('\n')
    f.close()
