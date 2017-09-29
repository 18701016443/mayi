#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/28 17:04
"""
from .base import Pyse

class MaYiQRPage(Pyse):
    '''PC网页二维码'''
    url = "/"


    #首页导航——APP首单立减5元——二维码
    def nav_qr(self):
        self.move_to_element("xpath=>/html/body/div[1]/div/ul/li[3]/div/a")
        QR_url = self.get_attribute("xpath=>/html/body/div[1]/div/ul/li[3]/div/div/img","src")
        return QR_url

    #下载页——下载按钮
    def down_btn(self):
        self.click("xpath=>/html/body/section/div[1]/div/a")

    #谷歌下载页面文案打印
    def text(self):
        text = self.get_text("xpath=>/html/body")
        return text

