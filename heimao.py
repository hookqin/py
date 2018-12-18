
#-*- coding: UTF-8 -*-

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
	

# df = pd.DataFrame(pd.read_excel('shushu.xlsx'))

# print(df)
# 
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

from bs4 import BeautifulSoup

# df.to_excel('excel_to_python.xlsx', sheet_name='bluewhale_cc') 
import time
from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://tousu.sina.com.cn/")
# time.sleep(2)

# soup = BeautifulSoup(driver.page_source,"html5lib")
# 
op = open('最热投诉.txt')
ff=op.read()
op.close()
soup = BeautifulSoup(ff,"html5lib")



# print(driver.page_source)
# ees=driver.page_source
# ko=driver.find_element(By.xpath("//<div class="))
# time.sleep(3)
# soup = BeautifulSoup(ees)

# # print(soup.h1)
# for xx in soup.select('h1'):
# 	print(xx.text)	
# shijian = re.findall(r'</span><span class="time">(.*?)</span>', ees)

# for xx in soup.select('.blackcat-con h1'):
# 	ki=xx.text
# 	print(ki)	

name = soup.select('.blackcat-con .name')
# print(name[ii].text)
tit = soup.select('.blackcat-con .time')
# print(tit[ii].text)

biaoti = soup.select('.blackcat-con h1')
# print(biaoti[ii].text)
uuu = soup.select('.blackcat-con p')
# print(uuu[ii].text)
# for nei in soup.select('.blackcat-con p'):
# 	rong=nei.text
tousuu = soup.select('.list')
# print(tousuu[0].text)
# touss = tousuu.replace('[投诉对象]','')
# touss = tousuu.replace('[投诉要求]','麤麤')
# 	print(rong)	
# 	
ii=0
for io in soup.select('.blackcat-con p'):
# urp = soup.select('.blackcat-con a .box select')
# print(urp[1].text)
# zhuangtai = soup.select('.blackcat-con .icon-status icon-yel')
# print(zhuangtai[ii].text)
	# print(tousuu[ii].text)

	print('处理到'+str(ii))
	# tousuu = soup.select('.list')
	# touss = tousuu[ii].text
	touss = tousuu[ii].text.replace(' [投诉对象]','')
	touss = touss.replace(' [投诉要求]','麤麤')
	# print(touss)
	# tousu = touss.split()
	# print(touss)
	# print(tousu[ii].text)
	yihang = name[ii].text+'麤麤'+tit[ii].text+'麤麤'+biaoti[ii].text+'麤麤'+uuu[ii].text+'麤麤'+touss
	yihang = yihang.replace('\n','')
	# print(yihang)
	ii=ii+1
	f = open('最热的.txt','a',encoding='utf-8')
	f.write(yihang+"\n")
	f.close()
# print(shijian[0])

# k = re.findall(r'</span></div>  <h1>(.*?)</h1>', ees)
# print(ees)
print('OK')

# driver.quit()
# print(ko)