import requests
#http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key=API&bk_length=600
import json
import csv
import difflib
from numba import njit

# print(1)
def web(a):
    r = requests.get('https://api.ownthink.com/kg/ambiguous?mention='+a)
    r2 = eval(r.text)
    return r2['data']
import time
#import sys
#import csv
import random as re

# @njit(forceobj=True)
def lxss(a,fw2,fw1,ll):
    fww = fw2
    fw = fw1
    def xsd(s1, s2):
        return difflib.SequenceMatcher(None, s1, s2).quick_ratio()
    r = []
    with open('D:\图片\小思框架\l第十一代\ownthink_v2.csv', 'r', encoding='utf8') as fin:
      reader = csv.reader(fin)
      # print('开始检索信息...',str(time.localtime()[3])+':'+str(time.localtime()[4]))
      i = 0
      #print('格式转换中...')
      #reader = list(reader)
      #reader = reader[fww:]
      #print('转换完毕。')
      #reader2 = reader#list(reader.replace('\0', ''))[fw2:fw1]
      for read in reader:
        #print(read)
        '''
        if i < fww:
            continue
        '''
        if xsd(a,read[0]) >= 0.41 and not read in ll:
            # print('搜索到子结果:',read)
            r.append(read)
        
        if i > fw :
            break

        i += 1
        #print(i,fw)
    # print('检索完毕。',str(time.localtime()[3])+':'+str(time.localtime()[4]))
    return r

# @njit(forceobj=True)
def find(w,len_=45):
    li1 = []
    try:
        a = 0
        for i in range(11):
            lx = lxss(w,a,a+10000,li1)
            if lx != []:

                li1+=lx
                # print('搜索到结果,目前长度:',len(li1))
            a += 10000
            if len(li1)>len_:
                # print('长度达到，返回结果。')
                break
            
    except KeyError:
        print('Error',i)
    
    return li1

if __name__ == '__main__':
    for i in find('香蕉'):
        print(i)
