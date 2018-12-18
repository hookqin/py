
#-*- coding: utf-8 -*-

import requests
#48 from sklearn import datasets
import numpy as np
import pandas as pd
# iris = datasets.load_iris()
# # print(iris.data)
# qq=pd.DataFrame(iris.data)
# print(qq.head())
# 
import re
# 
import time
# 
# def function(url):
		
# 	# url="https://ts.voc.com.cn/category/view/1/1.html"
# 	res=requests.get(url).text
# 	# print(res)
# 	m = re.findall(r'                   <a href="(.*?)" target="_blank">', res)
# 	# k = re.findall(r'<td>(.*) </td>', res)
# 	# print(k)
# 	# print("https://ts.voc.com.cn"+m[0])
# 	# print(len(m))
# 	print(m)
# 	for i in m:
# 		f = open('test.txt','a')
# 		f.write("https://ts.voc.com.cn"+i+"\n")
# 		f.close()

import xlrd
import openpyxl
import jieba
# # x=1
# for x in range(1,201):
# 	url="https://ts.voc.com.cn/category/view/1/"+str(x)+".html"
# 	# print(url)
# 	function(url)
# 	time.sleep(5)
	

df = pd.DataFrame(pd.read_excel('jieba.xlsx'))

# print(df)

jii = open('jieba.txt',"r",encoding="gbk").read()
# jii = jie.read()
# jie.close()

# print(jii)
jie=jieba.lcut(jii,cut_all=False)

counts={}
for word in jie:
	if len(word)==1:
		continue
	elif word=="电话" or word=="打电话":
		rword="电话"
	elif word=="退款" or word=="还款":
		rword="退款"
	else:
		rword=word
	counts[rword] = counts.get(rword,0) + 1

delword={"我们","他们","现在","10","2018","11","一个","当时","什么","本人","已经","然后","希望","投诉","时间","这个","就是","一直","可以","但是","结果","这样","工作","人员","时候","知道","因为","公司"}
for word in delword:
	del counts[word]


items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)  #降序排序次数
for i in range(15):
	word,count = items[i]
	# print("{0:<10}{1:>5}".format(word,count))
	print(word,count)
# print(jie)
#删除带有空值的行数据
# df.dropna(axis=0, how='any', inplace=True)
# print(df)

# op = open('shuju.txt')
# ff=op.read()
# op.close()
# fff=ff.split("\n")
# print(fff[0])
# shua=[]
# for x in fff:
# 	shua=x.split("$$")+shua

# try:
# 	# print(shua[3])
# 	qq=pd.DataFrame(fff)
# 	# print(qq.head)
# 	print(qq.isnull)
# except Exception as e:
# 	pass



# df.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc') 

