# -*- coding: utf-8 -*-
# 构造数据
from OperateCSV import class_csv
data1=[1,2,3,4,5,6]
data2=[2,3,4,5]
data3=[4,5,7,8,9,0,8]
data=[data1,data2,data3]

csv_file='\\test.csv'
myCSV=class_csv.CSV_operation(csv_file)

myCSV.open_for_addData()
for i in data:
    myCSV.write_csv(i)
myCSV.close_file_write()

myCSV.open_for_read()
myCSV.read_csv()
myCSV.close_file_read()