#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 10:46
"""
from .base import Pyse
from models import mydef

class LandlordConfirmPage(Pyse):
    '''待确认订单'''

    #待确认订单
    def confirm(self):
        self.click("id=>confirm")

    #确认
    def confirm_btn(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[6]/p[1]/input")

    #确认订单弹窗——确定
    def alert_confirm(self):
        self.click("xpath=>html/body/div[16]/div/div/div/div[2]/div[2]/input[1]")


    #确认订单弹窗——以后再说
    def cancel(self):
        self.click("xpath=>html/body/div[16]/div/div/div/div[2]/div[2]/input[2]")

    #拒绝
    def refuse(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[6]/p[2]/a")

    #拒绝理由
    def refuse_reason(self):
        self.click("xpath=>html/body/div[17]/div[2]/div[2]/form/label["+ mydef.rad_num(1,9) +"]")

    #拒绝订单
    def refuse_order(self):
        self.click("xpath=>html/body/div[17]/div[2]/div[2]/form/input[1]")

    #取消
    def refuse_cancel(self):
        self.click("xpath=>html/body/div[17]/div[2]/div[2]/form/input[2]")

    #联系房客
    def call_tenant(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[6]/span/span[1]/a")

    #房客主页
    def tenant_index(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[6]/p[3]/a")

    #订单列表状态
    def status(self):
        text = self.get_text("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[5]/p[1]/span")

    #订单详情页
    def order_details(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[2]/div/div/div[2]/div[5]/p[2]/a")

    #返回我的订单
    def return_myorder(self):
        self.click("xpath=>html/body/div[14]/div/div/div[1]/div[2]/a")

    #订单详情页的确认
    def order_details_confirm(self):
        self.click("xpath=>html/body/div[14]/div/div/div[2]/div[1]/div/input")

    #订单详情页的确认弹窗——确认
    def alert_order_details_confirm(self):
        self.click("xpath=>html/body/div[24]/div/div/div/div[2]/div[2]/input[1]")

    #订单详情页的确认弹窗——以后再说
    def alert_order_details_cancel(self):
        self.click("xpath=>html/body/div[24]/div/div/div/div[2]/div[2]/input[2]")

    #订单详情页的拒绝
    def order_details_refuse(self):
        self.click("xpath=>html/body/div[14]/div/div/div[2]/div[1]/div/span/a")

    # 订单详情页的拒绝——拒绝订单理由
    def alert_details_refuse_reason(self):
        self.click("xpath=>html/body/div[27]/div[2]/div[2]/form/label["+mydef.rad_num(1,9)+"]")

    # 订单详情页的拒绝——拒绝订单按钮
    def alert_details_refuse_order(self):
        self.click("xpath=>html/body/div[27]/div[2]/div[2]/form/input[1]")

    # 订单详情页的拒绝——取消按钮
    def alert_details_refuse_cancel(self):
        self.click("xpath=>html/body/div[27]/div[2]/div[2]/form/input[2]")

    #订单详情页的状态
    def order_details_status(self):
        text = self.get_text("xpath=>html/body/div[14]/div/div/div[2]/div[1]/p/span")

