# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/16 7:11
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : practice.py
# @Software : PyCharm

import requests
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    #指定url
    url = 'https://movie.douban.com/j/search_subjects?'
    params = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit':'40',
        'page_start':'0',
    }
    #发送请求
    response = requests.get(url=url,params=params,headers=headers)
    #获取响应
    page_json = response.json()
    #持久化存储

    fp=open('./豆瓣.json','w',encoding='utf-8')
    json.dump(page_json,fp,ensure_ascii=False)

    print("success!!!")