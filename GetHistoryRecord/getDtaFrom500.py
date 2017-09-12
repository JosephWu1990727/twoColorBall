# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
class AnalysisHtml(object):
    def __init__(self,html_file):
        self.file=html_file # store HTML file
        self.soup=BeautifulSoup(self.file,"html.parser") # open html file, and creat BS4 object

    def getTargetNum(self):
        dataTable=self.soup.find_all("tr",align="center")
        Num=dataTable[0].find_all(class_="ball_box01")[0].find_all("li")
        targetNum=[]
        for i in Num:
            targetNum.append(i.get_text().encode('utf-8'))
        num2=dataTable[0].find_all("table")[0].find_all("tr")[1].find_all("td")[1].get_text()
        targetNumByOrder=num2.encode('utf-8').split()
        return targetNum,targetNumByOrder

    def getAllIndexnum(self):
        rawdata=self.soup.find_all("span",class_="iSelectBox")
        rawdatalist=rawdata[0].find_all('div')[0].find_all('a')
        targetlist=[]
        for i in rawdatalist:
            targetlist.append(i['href'].encode('utf8'))
        return targetlist
