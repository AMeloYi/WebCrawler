import urllib.request
import http.cookiejar
# ------------- GET 的时候添加 header -------------------------------

# ---- 方法 1 -------------------------
# 方法比较简便直接，但是不好扩展功能
'''
url = 'http://www.baidu.com/'
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})

oper = urllib.request.urlopen(req)
data = oper.read()
print(data.decode())
'''
# ---- 方法 2 --------------------------
# 使用 build_opener
def makeMyOpener(head = {
'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout= 1000)
data = uop.read()
print(data.decode())