#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 16:28
"""
from .base import Pyse

class LandlordMicroshopPage(Pyse):
    '''微店订单'''
    utl = "/"

    #微店订单
    def microshop(self):
        self.click("id=>microshop")

    def status(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[1]/span")
        return text

    #订单详情
    def microshop_order_details(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[2]/a")

    #订单详情页的状态
    def microshop_order_details_status(self):
        text = self.get_text("xpath=>/html/body/div[14]/div/div/div[2]/div[1]/p/span")
        return text

    #返回我的订单
    def microshop_return_myorder(self):
        self.click("xpath=>/html/body/div[14]/div/div/div[1]/div[2]/a")
