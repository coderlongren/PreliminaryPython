# -*- coding: utf-8 -*-
import xlrd
import os
import pymysql
import json
import codecs
from random import shuffle

def open_excel(file = 'file.xls'):#打开要解析的Excel文件
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def excel_by_index(file = 'file.xls', colindex = 0, by_index = 0):#按表的索引读取
    data = open_excel(file)#打开excel文件
    tab = data.sheets()#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    colName = tab.row_values(colindex)#第0行的值
    list = []#创建一个空列表
    for x in range(0, nrows):
        row = tab.row_values(x)
        if row:
            app = {}#创建空字典
            for y in range(0, ncols):
                app [ colName[y] ] = row[y]
            list.append(app)
    return list

def read_excel(file = 'file.xls', by_index = 0):#直接读取excel表中的各个值
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    for x in range(0, nrows):
         for y in range(0, ncols):
             value = tab.cell(x,y).value
             print(tab.cell(x, y).value)
def main():
    f = codecs .open(r'E:\besttoefl.txt' , 'w' , 'utf-8' )
    # print('input the path of your file:')
    a = open_excel(r'E:\\toefl.xls')
    # sh = a.sheet_by_name('')
    sh = a.sheet_by_index(0) # 第一个Sheet
    # sheetNames = a._sheet_names()
    # print(sheetNames)
    list = []
    cellA1 = sh.cell(1,0)
    print(cellA1.value)
    columvalues1 = sh.col_values(0) # 第一列
    columvalues2 = sh.col_values(1) # 第二列
    columvalues3 = sh.col_values(2) # 第二列
    columvalues4 = sh.col_values(3) # 第二列
    columvalues2 = sh.col_values(4) # 第二列
    columvalues2 = sh.col_values(1) # 第二列

    # print(columvalues2)
    # print(len(columvalues1))
    # print(len(columvalues2))
    i = 0
    while i < 2080:
        if sh.cell(i,0).value == "":
            i= i + 1
            continue
        list.append(sh.cell(i,0).value + " " + sh.cell(i,1).value)
        i = i + 1

    i= 0
    while i < 2000:
        if sh.cell(i,2).value == "":
            i= i + 1
            continue
        list.append(sh.cell(i,2).value + " " + sh.cell(i,3).value)
        i = i + 1

    i= 0
    while i < 2000:
        if sh.cell(i,4).value == "":
            i= i + 1
            continue
        list.append(sh.cell(i,4).value + " " + sh.cell(i,5).value)
        i = i + 1
    # for line in list:
    #     print(line)
    #
    print(len(list))
    shuffle(list) # 乱序

    for line in list:
        f.write(line + "\n")

    # print(a)
    # b = excel_by_index(r'E:\\toefl.xls', 0, 0)
    # m = []
    # for i in range(b.__len__()):
    #     c = b[i]
    #     # a = c['name']
    # for x in c:
    #     if x == 'date':
    #         print(x)
    # print('meng')
    # read_excel(r'D:\smt_ioe\untitled\analysis_excel\my.xls',2)

if __name__ == '__main__':
    main()