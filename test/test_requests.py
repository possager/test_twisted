import requests
from twisted.internet import reactor,defer
from twisted.web.client import getPage,downloadPage
from twisted.python.util import InsensitiveDict
from twisted.web.client import Headers





url1='https://www.baidu.com'

headers={
    b'User-Agent':[b'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'],
    b'Upgrade-Insecure-Requests':[b'1'],
    b'Accept':[b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'],
    b'Accept-Encoding':[b'gzip, deflate, br'],
    b'Accept-Language':[b'zh-CN,zh;q=0.9'],
    b'Host':[b'www.baidu.com'],
}


headers1=InsensitiveDict()

headers1[b'User-Agent']=b'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
headers1[b'Upgrade-Insecure-Requests']=b'1'
headers1[b'Accept']=b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
headers1[b'Accept-Encoding']=b'gzip, deflate, br'
headers1[ b'Accept-Language']=b'zh-CN,zh;q=0.9'
headers1[b'Host']=b'www.baidu.com'


headers2=Headers(rawHeaders=headers)



resposne1=requests.get(url=url1)
print(resposne1.text)

d1=getPage(bytes(url1,encoding='utf-8'))
def showresult(data):
    print(data)
    reactor.stop()


d1.addCallback(showresult)

reactor.run()