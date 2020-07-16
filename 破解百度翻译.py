# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/15 18:49
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 破解百度翻译.py
# @Software : PyCharm
#怎么正确的找到url, 局部页面刷新:ajax
import requests
import json
if __name__ == '__main__':
    word = input('Enter an word:\n')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    #指定url
    url = 'https://fanyi.baidu.com/sug'
    #封装post请求参数，如果请求携带了参数，则将参数封装到字典中结合requests请求方法中params参数进行url的处理
    data = {
        'kw':word,
    }
    #发起请求
    response = requests.post(url=url,data=data,headers=headers)

    #获取响应数据
    filename = word + '.json'
    json_data = response.json()
    fp = open(filename,'w',encoding='utf-8')
    json.dump(json_data,fp,ensure_ascii=False)
