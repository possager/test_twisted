# from twisted.web.client import getPage
from twisted.internet import reactor
from Mytwiste_http_client import getPage1,getPage2




url = b'http://www.baidu.com'

urlist1=['https://www.mala.cn/forum-70-{}.html'.format(str(i)) for i in range(1,500)]





def print_and_stop(output):
    print (output)
    url=str(output['url'],encoding='utf-8')
    page=output['page']

    try:
        filename=url.split('-')[-1]
        filepath='F:/test_data/test1/'

        with open(filepath+filename,'wb') as fl:
            fl.write(page)
    except Exception as e:
        print(e)

    # if reactor.running:
    #    reactor.stop()

if __name__ == '__main__':
    for one_url in urlist1:
        print ('fetching', one_url)
        d = getPage1(bytes(one_url,encoding='utf-8'))
        d.addCallback(print_and_stop)
    reactor.run()