from twisted.internet import reactor,defer
from twisted.web.client import getPage,downloadPage
# from Mytwiste_http_client import getPage1
from twisted.python.util import InsensitiveDict



url1=b'https://www.badiu.com'


# headers1=InsensitiveDict()
# headers1[b'User-Agent']=b'JiemianNews/5.1.0 (android; android 4.4.4; ONEPLUS A3010)'
# headers1[b'Content-Type']:b'application/x-www-form-urlencoded'
# headers1[b'Host']=b'appapi.jiemian.com'
headers1={
    b'User-Agent':b'JiemianNews/5.1.0 (android; android 4.4.4; ONEPLUS A3010)',
    b'Content-Type':b'application/x-www-form-urlencoded',
    b'Host':b'appapi.jiemian.com',
    b'Connection':b'close'
}


board_url=b'http://appapi.jiemian.com/v4/5.1.0/10001/cate/117/0/1/51/5101.json?vid=861557177515977&dv=android&os=4.4.4&rl=720*1280&ac=WIFI'

def showresult(result):
    print(result)




d1=getPage(url=board_url,headers=headers1,agent=b'JiemianNews/5.1.0 (android; android 4.4.4; ONEPLUS A3010)',method=b'GET')

d1.addCallback(showresult)

reactor.run()