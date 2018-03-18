from twisted.internet import reactor,defer
from twisted.web.client import getPage,downloadPage
# from Mytwiste_http_client import getPage
import time




def deal_page(result):
    # page=result['page']
    # url=result['url']

    # fielname=url.split('_')[-1]
    # print(url,'has been down.......')
    timestr=str(time.time()*1000)



    # with open('/media/slience-liang/3804CCCA04CC8C76/test_data/test1/'+timestr,'rb') as fl:
    with open('F://test_data/test1/'+timestr,'rb') as fl:
        fl.write(result)

    reactor.stop()



urlist1=['https://www.mala.cn/forum-70-{}.html'.format(str(i)) for i in range(1,2)]

# for oneurl in urlist1:
#     boneurl=(bytes(oneurl,encoding='utf-8'))
#     print(boneurl)
#
#     d1=getPage(url=boneurl)
#     d1.addCallback(deal_page)
#     # reactor.callWhenRunning(d1.callback,)
#
#     reactor.run()

d1=getPage(url=b'https://www.baidu.com')
d1.addCallback(deal_page)

reactor.run()