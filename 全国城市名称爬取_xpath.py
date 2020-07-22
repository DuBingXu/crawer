# !/user/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/7/22 9:30
# @Author   : Du BingXu
# @Email    : adubingxu@163.com
# @File     : 全国城市名称爬取_xpath.py
# @Software : PyCharm

import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers)
    tree = etree.HTML(page_text)
    host_li_list = tree.xpath('//div[@class="bottom"]//li')
    for li in host_li_list:
        host_name = li.xpath('./a/text()')[0]














