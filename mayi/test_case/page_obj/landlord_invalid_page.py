#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 16:11
"""
from .base import Pyse

class LandlordInvalidPage(Pyse):
    '''失效订单'''
    url = "/"

    #失效订单
    def invalid(self):
        self.click("id=>invalid")

    #订单状态
    def status(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[1]/span")
        return text

    #订单详情
    def invalid_order_details(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[2]/a")

    #订单详情页——返回我的订单
    def invalid_return_my_order(self):
        self.click("xpath=>/html/body/div[14]/div/div/div[1]/div[2]/a")

    #订单详情页——订单状态
    def invalid_order_details_status(self):
        text = self.get_text("xpath=>/html/body/div[14]/div/div/div[2]/div[1]/p/span")
        return text
