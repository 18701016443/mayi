#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 9:17
"""
from .base import Pyse

class LandlordOfflinePage(Pyse):
    '''房源下线'''
    url = "/"

    #房源下线
    def room_offline(self):
        self.click("xpath=>html/body/div[13]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[4]/a")

    #下线原因
    def offline_reason(self,num):
        self.click("xpath=>html/body/div[19]/div/div/div/div[2]/div[2]/div/label["+num+"]")

    #操作下线
    def offlineReasonBtn(self):
        self.click("id=>offlineReasonBtn")

    #下线房源弹窗——我知道了
    def okOfflineSuccessBtn(self):
        self.click("id=>okOfflineSuccessBtn")

    #下线房源弹窗——“下线成功”文案
    def offlineSuccess_text(self):
        text = self.get_text("xpath=>html/body/div[20]/div/div/div/div[2]/div[1]")
        return text

    #关闭
    def cancelOfflineReasonBtn(self):
        self.click("id=>cancelOfflineReasonBtn")

    #下线房源弹窗-我要下线
    def offlineBtn(self):
        self.click("id=>offlineBtn")

    #下线房源弹窗-去价格房态
    def gopriceCal(self):
        self.click("id=>gopriceCal")

    #下线房源弹窗文案
    def offline_text(self):
        text = self.get_text("xpath=>html/body/div[18]/div/div/div/div[2]/div[1]/div")
        return text
