# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/15 16:11
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 简易网页采集器.py
# @Software : PyCharm

# ！！！！找url时注意，从问号分开，注意键值

#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测为某一浏览器，说明正常请求，若不是则不正常

import requests

if __name__ == '__main__':
    # 伪装：让爬虫对应的请求身份标识伪装成某一浏览器
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典
    kw = input('Enter a world：n')
    param = {
        'query':kw
    }
    #发起请求对应的url是携带参数的，请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    #获取响应数据
    page_text = response.text
    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)

    print(filename,'保存成功')



