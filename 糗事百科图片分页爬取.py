# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/17 7:44
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 糗事百科图片.py
# @Software : PyCharm

import requests
import re
import os

if __name__ == '__main__':
    #创建一个文件夹保存图片
    if not os.path.exists('./qiutulibs'):
        os.mkdir('./qiutulibs')
    #如何爬取图片数据
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }

    #url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1,4):
        new_url = format(url%pageNum)
        #content返回的是二进制形式的图片数据
        #text（返回字符串）json（）（对象）content（二进制）

        #使用通用爬虫对url对应的一整张页面进行爬取
        page_text = requests.get(url=new_url,headers=headers).text

        #使用聚焦爬虫对将页面中所有的图片进行解析/提取
        #对url进行分析
        # <div class="thumb">
        # <a href="/article/123354065" target="_blank">
        # <img src="//pic.qiushibaike.com/system/pictures/12335/123354065/medium/5SMNEOVW8PDFH6H1.jpg" alt="糗事#123354065" class="illustration" width="100%" height="auto">
        # </a>
        # </div>
        #https://pic.qiushibaike.com/system/pictures/12335/123357460/medium/0XYPUMHCHFJ2DIQG.jpg

        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'#正则表达式
        img_src_list = re.findall(ex,page_text,re.S)#re.S多行匹配
        #print(img_src_list)
        for src in img_src_list:
            src = 'https:' + src #拼接完整的url
            #请求到图片的二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名字
            img_name = src.split('/')[-1]
            img_path = './qiutulibs/'+img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data)
                print(img_name,' 打印成功')



