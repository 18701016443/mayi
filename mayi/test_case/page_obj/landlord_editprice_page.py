#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 15:28
"""

from .base import Pyse

class LandlordEditpricePage(Pyse):
    '''审核中——修改价格'''

    #审核中
    def roomfilter2(self):
        self.click("id=>roomfilter2")

    #修改价格
    def edit_price(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[1]/a")

    #特殊价是否参与打折
    def specialdiscount_yes(self):
        self.click("xpath=>html/body/div[15]/div/div/div/div[2]/ul/li[5]/input[1]")
    def specialdiscount_no(self):
        self.click("xpath=>html/body/div[15]/div/div/div/div[2]/ul/li[5]/input[2]")

    #修改价格弹窗——确定
    def confirmModifyPriceBtn(self):
        self.click("id=>confirmModifyPriceBtn")

    ##修改价格弹窗——取消
    def cancelModifyPriceBtn(self):
        self.click("id=>cancelModifyPriceBtn")

    #修改价格弹窗文案
    def editsuccess_text(self):
        text = self.get_text("xpath=>html/body/div[16]/div/div/div/div[2]/div[1]")
        return text
    #修改价格弹窗——我知道了
    def changePriceSuccessBtn(self):
        self.click("id=>changePriceSuccessBtn")