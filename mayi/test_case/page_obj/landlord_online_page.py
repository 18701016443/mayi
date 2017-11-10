#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 10:18
"""
from .base import Pyse

class LandlordOnlinePage(Pyse):
    '''房源上线'''
    url = "/"

    #已下线
    def roomfilter5(self):
        self.click("id=>roomfilter5")

    #房源上线
    def room_online(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[4]/a")

    #房源上线——成功文案
    def onlinesuccess_text(self):
        text = self.get_text("xpath=>html/body/div[17]/div/div/div/div[2]/div[1]")
        return text

    #房源上线成功——我知道了
    def onlineSuccessBtn(self):
        self.click("id=>onlineSuccessBtn")