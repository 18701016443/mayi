#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 16:57
"""
from .base import Pyse

class LandlordRoomsearchPage(Pyse):
    '''结算管理房间搜索'''

    def rooms(self):
        self.get_elements("xpath=>//*[@id='lodgeunitid']/option")

    #按房间搜索
    def lodgeunitid(self,num):
        self.click("xpath=>//*[@id='lodgeunitid']/option["+num+"]")

    #搜索
    def search(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[2]/input")

    #详情
    def details(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[9]/a")

    #关闭
    def closeModifyPriceBtn(self):
        self.click("id=>closeModifyPriceBtn")

    #支付宝查账说明
    def alipayprompt(self):
        self.open_new_window("xpath=>/html/body/div[14]/div[5]/div/div[2]/div[1]/a")
