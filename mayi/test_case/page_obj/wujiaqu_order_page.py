#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 16:59
"""
from .base import Pyse
from mayi.models import mydef

class WujiaquOrderPage(Pyse):
    '''五家渠下订单'''
    url = "/wujiaqu/"

    #关键词
    def searchcityin1(self):
        searchcityin1 = "张佳恒测试"
        self.type("id=>searchcityin1",searchcityin1)

    #搜索
    def landmarkBtn(self):
        self.click("id=>landmarkBtn")

    #第一个房源
    def one_room(self):
        list = []
        dds = self.get_elements("xpath=>//*[@id='searchRoom']/dd")
        for i in dds:
            id = i.get_attribute("lid")
            list.append(id)
        self.open_new_window("xpath=>//*[@id="+list[0]+"]")

    #立即预定
    def goBookBtn(self):
        self.click("id=>goBookBtn")

    #入住人数
    def people(self):
        people = mydef.rad_num(1,10)
        self.type("xpath=>html/body/form/div[2]/div[1]/div[1]/div/div/dl[3]/dd/input[2]",people)

    #入住人姓名
    def tenantname(self):
        tenantname = mydef.rad_word(5)
        self.clear("id=>tenantname")
        self.type("id=>tenantname",tenantname)

    def name(self):
        n = self.get_text("id=>tenantname")
        return n

    # def phone(self):
    #     ph ="15539243368"
    #     self.clear("id=>tenantmobile")
    #     self.type("id=>tenantmobile",ph)
    def xiug(self):
        self.click("id=>editMobile")

    #保险联系人
    def user(self):
        self.click("xpath=>//*[@id='insuranceDiv']/div/div[1]/div[1]/div/ul/li[1]/div/div[1]/span")

    #提交订单
    def submit_order(self):
        self.click("xpath=>html/body/form/div[2]/div[1]/div[6]/div/a")

    #订单提交成功后返回的文案
    def order_success(self):
        text = self.get_text("xpath=>//*[@id='payForm']/div/div[1]/div[2]/p[1]")
        return text

