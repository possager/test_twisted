from twisted.internet import reactor,defer
# from twisted.web.client import getPage
from twisted.web.client import downloadPage,HTTPClientFactory
from twisted.web.client import URI,nativeString




class LL_HTTPClientFactory(HTTPClientFactory):
    def page(self, page):
        if self.waiting:

            _ = {
                'page':page,
                'headers':self.headers,
                'response_headers':self.response_headers,
                'cookies':self.cookies,
                'status':self.status,
                'url':self.url
            }


            self.waiting = 0
            self.deferred.callback(_)




def _makeGetterFactory(url, factoryFactory, contextFactory=None,
                       *args, **kwargs):
    """
    Create and connect an HTTP page getting factory.

    Any additional positional or keyword arguments are used when calling
    C{factoryFactory}.

    @param factoryFactory: Factory factory that is called with C{url}, C{args}
        and C{kwargs} to produce the getter

    @param contextFactory: Context factory to use when creating a secure
        connection, defaulting to L{None}

    @return: The factory created by C{factoryFactory}
    """
    uri = URI.fromBytes(url)
    factory = factoryFactory(url, *args, **kwargs)
    if uri.scheme == b'https':
        from twisted.internet import ssl
        if contextFactory is None:
            contextFactory = ssl.ClientContextFactory()
        reactor.connectSSL(
            nativeString(uri.host), uri.port, factory, contextFactory)
    else:
        reactor.connectTCP(nativeString(uri.host), uri.port, factory)
    return factory




def getPage1(url, contextFactory=None, *args, **kwargs):
    """
    Download a web page as a string.

    Download a page. Return a deferred, which will callback with a
    page (as a string) or errback with a description of the error.

    See L{HTTPClientFactory} to see what extra arguments can be passed.
    """
    return _makeGetterFactory(
        url,
        LL_HTTPClientFactory,
        contextFactory=contextFactory,
        *args, **kwargs).deferred



def getPage2(url,contentFactory=None,*args,**kwargs):
    return _makeGetterFactory(
        url,
        HTTPClientFactory,
        contextFactory=contentFactory,
        *args,**kwargs
    ).deferred