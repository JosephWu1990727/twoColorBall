# -*- coding: UTF-8 -*-
# 封装好BS4的内容用于使用
# 以后若需要爬取新的页面，只需要分析页面结构在此文件里面填写新的行数即可
#
import re
from bs4 import BeautifulSoup
class AnalysisDetailPageHtml(object):
    'this is crawler due to BS4'
    def __init__(self,html_file):
        self.file=html_file # store HTML file
        self.soup=BeautifulSoup(self.file,"html.parser") # open html file, and creat BS4 object


    def getDate(self):
        data=self.soup.find_all()

