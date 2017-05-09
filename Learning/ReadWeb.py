# encoding:UTF-8
import urllib
import urllib.request

'''
# Simple method
url = "http://www.baidu.com"
data1 = urllib.request.urlopen(url).read()
data1 = data1.decode('UTF-8')
print(data1)
'''
'''
# HTTPReponse Object
a = urllib.request.urlopen(url)
print(type(a))
print(a.geturl())
print(a.info())
print(a.getcode())
'''
# 简单处理URL(抓取搜索关键词为sina的网页)
data2 = {}
data2['word'] = 'sina'
url_values = urllib.parse.urlencode(data2)
url = "http://www.baidu.com/s?"
full_url = url + url_values

data2 = urllib.request.urlopen(full_url).read()
data2 = data2.decode('UTF-8')
print(data2)
