# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/21 17:14
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 58二手房_xpath.py
# @Software : PyCharm
#爬取58二手房的房源信息
from lxml import etree
import  requests
if __name__ == '__main__':
    #爬取网页源码数据
    url = 'https://zmd.58.com/ershoufang/h1/?PGTID=0d30000c-0042-b93b-4b47-31d62f4799dc&ClickID=1'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text

    #数据解析
    #实例化etree对象
    tree = etree.HTML(page_text)
    title_list = []
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    for li in li_list:
        title = li.xpath('./div[2]//a/text()')[0] #.表示当前解析出li指向的2局部源码内容
        title = title
        title_list.append(title)

    for title in title_list:

        print(title+'\n')


