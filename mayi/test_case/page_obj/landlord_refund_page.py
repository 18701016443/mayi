#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 15:38
"""
from .base import Pyse

class LandlordRefundPage(Pyse):
    '''退款订单'''

    url = "/"

    #退款订单
    def refund(self):
        self.click("id=>refund")

    #订单详情
    def refund_order_defails(self):
        self.click("xpath=>/html/body/div[13]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[2]/a")

    #订单状态
    def status(self):
        text = self.get_text("xpath=>/html/body/div[13]/div[5]/div/div[2]/div/div[1]/div[2]/div[5]/p[1]/span")
        return text

    #订单详情页——返回我的订单
    def refund_return_my_order(self):
        self.click("xpath=>/html/body/div[13]/div/div/div[1]/div[2]/a")

    #订单详情页——订单状态
    def refund_order_details_status(self):
        text = self.get_text("xpath=>/html/body/div[13]/div/div/div[2]/div[1]/p/span")
        return text