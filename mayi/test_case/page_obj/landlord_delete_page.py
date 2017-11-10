#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 10:00
"""

from .base import Pyse

class LandlordDeletePage(Pyse):
    '''房源删除'''
    url = "/"

    #已下线
    def roomfilter5(self):
        self.click("id=>roomfilter5")

    #审核中
    def roomfilter2(self):
        self.click("id=>roomfilter2")

    #未通过
    def roomfilter3(self):
        self.click("id=>roomfilter3")

    #未完善
    def roomfilter1(self):
        self.click("id=>roomfilter1")

    #已上线/已下线——房源删除
    def room_delete(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[2]/a")
    #审核中/未通过——房源删除
    def checking_delete(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[3]/a")

    #待完善——房源删除
    def need_complete_delete(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[2]/a")

    #删除房源弹窗-确定
    def delBtn(self):
        self.click("id=>delBtn")

    #删除房源—取消
    def cancelDelBtn(self):
        self.click("id=>cancelDelBtn")

    #删除房源——我知道了
    def okDelSuccessBtn(self):
        self.click("id=>okDelSuccessBtn")

    #已上线/已下线/未通过/待完善/审核中——删除房源成功文案
    def delsuccess_text(self):
        text = self.get_text("xpath=>html/body/div[25]/div/div/div/div[2]/div[1]")
        return text

    # #审核中——删除房源成功文案
    # def checking_delsuccess_text(self):
    #     text = self.get_text("xpath=>html/body/div[25]/div/div/div/div[2]/div[1]")
    #     return text

