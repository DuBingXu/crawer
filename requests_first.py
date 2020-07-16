# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/15 15:49
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : requests_first.py
# @Software : PyCharm
# ---爬取搜狗首页数据---
import requests
if __name__ == "__main__":
    #step 1:指定url
    url = 'https://www.sogou.com/'
    #step 2:发起请求
    #get方法会相应一个响应对象
    response = requests.get(url=url)
    #step 3:获取响应数据,.text返回是字符串形式的响应数据
    page_text = response.text
    #step 4:持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')
