#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 20:58
"""
from .base import Pyse

class LandlordActivity(Pyse):
    '''活动设置'''
    # url = "/"

    #活动页面文案
    def text(self):
        text= self.get_text("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[1]/p")
        return text

    #活动好处
    def active_good(self):
        self.click("class=>active_good")

    #活动好处弹窗关闭按钮
    def img_close(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[4]/div[2]/img")

    #活动规则
    def regular_desc(self):
        self.click("class=>regular_desc")

    #活动规则弹窗文案
    def regular_desc_text(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[3]/div[2]")
        return text

    #活动规则弹窗关闭按钮
    def regular_desc_close(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[3]/div[2]/img")



