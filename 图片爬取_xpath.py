# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/22 8:28
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 图片爬取_xpath.py
# @Software : PyCharm
import os
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }

    #获取页源码数据

    page_text = requests.get(url=url,headers=headers).text
    #手动设定相应数据的编码格式
    # response.encoding = 'utf-8'
    # page_text =response.text
    #实例化etree对象
    tree = etree.HTML(page_text)
    #解析数据 src alt属性值
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    #创建文件夹
    if not os.path.exists('picLibs'):
        os.mkdir('./picLibs')

    for li in li_list:
        li_src = li.xpath('./a/img/@src')[0]
        #拼成完整的src地址
        li_src = 'http://pic.netbian.com' + li_src
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        #通用处理中文乱码的解决方案
        img_name = img_name.encode('iso-8859-1').decode('gbk')

        #请求图片，持久化存储
        img_data = requests.get(url=li_src,headers=headers).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'successful!!!')







