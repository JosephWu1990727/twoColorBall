# -*- coding: UTF-8 -*-
import zlib
import urllib2

def GetWebConent(TargetUrl,OtherCoff,Code):
    # TargetUrl => 是指需要进行爬虫爬取的目标网址
    # OtherCoff => 是一个字典类型，包含构造Url请求时候的其他参数
    print 'get web content, url is %s' % TargetUrl
    headers = { 'User-Agent' : OtherCoff['Agent']} # 获取字典OtherCoff里面的Agent属性
    request = urllib2.Request(TargetUrl,headers = headers)
    request.add_header('Accept-encoding', 'gzip')
    opener=urllib2.build_opener()
    response = opener.open(request)
    html = response.read()
    gzipped = response.headers.get('Content-Encoding')
    if gzipped:
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    return html