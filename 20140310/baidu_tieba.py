# -*- coding: cp936 -*-
#Fileanme:baidu_tieba.py
import string ,urllib2

def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page, end_page+1):
        sName = string.zfill(i,5)+ '.html'
        print '正在下载第' + str(i) + '个网页，并将其存储为' + sName + '..........'
        f = open (sName,'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()




bdurl = str(raw_input('url：  \n'))
begin_page = int(raw_input('begin :\n'))
end_page = int(raw_input('end : \n'))

baidu_tieba(bdurl,begin_page,end_page)
