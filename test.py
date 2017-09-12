# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-

from GetHistoryRecord import getDtaFrom500
from GetHistoryRecord import getWeb
from GetHistoryRecord.config import TargetMainUrl,CoffConf
from OperateCSV import class_csv
from OperateCSV.config import file_lottery_num,file_lottery_num_byOrder

Url=TargetMainUrl  #
Coff=CoffConf
# 实例化文件操作的类
# 记录中奖号码
myCSV_file_lottery_num=class_csv.CSV_operation(file_lottery_num)
myCSV_file_lottery_num.open_for_addData()
#记录中奖号码（按照顺序）
myCSV_file_lottery_num_byOrder=class_csv.CSV_operation(file_lottery_num_byOrder)
myCSV_file_lottery_num_byOrder.open_for_addData()
# 先打开一个目标网址
webCotent= getWeb.GetWebConent(Url, Coff,'utf-8')
my500_toGetUrlList=getDtaFrom500.AnalysisHtml(webCotent)
urlList=my500_toGetUrlList.getAllIndexnum()
# 从目标网址，分析得出详情页里面数据
for url in urlList:
    webDetailCotent=getWeb.GetWebConent(TargetUrl=url,OtherCoff=Coff,Code='utf-8')
    my500_toGetData=getDtaFrom500.AnalysisHtml(webCotent)
    [lottery_num,lottery_num_byOrder]=my500_toGetData.getTargetNum()
    # 根据数据，组装成字字典
    index_num=url.split('/')[-1].split('.')[0]
    lottery_num.insert(0,index_num)
    lottery_num_byOrder.append(lottery_num[-1]) # 把蓝色的球，加到按照顺序的球最后
    lottery_num_byOrder.insert(0,index_num)
    print lottery_num
    print lottery_num_byOrder

    myCSV_file_lottery_num.write_csv(lottery_num)
    myCSV_file_lottery_num_byOrder.write_csv(lottery_num_byOrder)

# 操作完，关闭文件
myCSV_file_lottery_num_byOrder.close_file_write()
myCSV_file_lottery_num.close_file_write()




