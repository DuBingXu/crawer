# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/16 8:16
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 药品监督管理总局化妆品生产许可证相关数据.py
# @Software : PyCharm
#动态加载数据，首页中对应的企业信息数据是通过ajax动态请求到的
    #对比详情页url发现，域名一样，id不一样
    #id可以从从首页对应的ajax请求的json串中获取
    #域名和id可以拼接处一个完整企业对于=应的详情页url
#详情页的企业详情数据也是动态加载出来的，参数为id值
    #观察发现
        #所有的post请求的url都一样，只有参数id值不一样
        #我们可以批量获取多家企业id，然后拼接成一个完整对应的ajax请求的url
import requests
import json
if __name__ =='__main__':
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    #ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    data_list = []#企业id
    all_data_list = []#存储所有企业详情数据
    #参数封装
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page':page,
            'pageSize':'15',
            'productName':'',
            'conditionType':'1',
            'applyname':'',
            'applysn':'',
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for d in json_ids['list']:
            data_list.append(d['ID'])

    #获取企业详情数据
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for ids in data_list:
        data = {
            'id': ids
        }
        detail_json = requests.post(url=post_url,data=data,headers=headers).json()#要加括号
       # print(detail_json)
        all_data_list.append(detail_json)

    #持久化存储
    fp = open('./all_data.json', 'w', encoding='utf-8')
    json.dump(all_data_list,fp=fp, ensure_ascii=False)
    print('success!!!')



