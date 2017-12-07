#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 9:36
"""
from .base import Pyse
from models import mydef

class LandlordExperiencePage(Pyse):
    '''特色体验'''

    #特色体验介绍
    def tsty_introduce(self):
        self.click("xpath=>html/body/div[14]/ul/a[2]")

    #创建新体验
    def new_tsty(self):
        self.click("xpath=>html/body/div[14]/ul/a[1]")

    #体验名称
    def title(self):
        title = mydef.rad_word(5)
        self.clear("id=>title")
        self.type("id=>title",title)

    #体验简介
    def introduction(self):
        text = mydef.rad_word(50)
        self.clear("id=>introduction")
        self.type("id=>introduction",text)

    #体验详情
    def details(self):
        text = mydef.rad_word(50)
        self.clear("id=>details")
        self.type("id=>details",text)

    #体验时长
    def experiencehour(self):
        self.click("xpath=>//*[@id='experiencehour']/option["+mydef.rad_num(1,14)+"]")
    #时长单位
    def timeWay(self):
        self.click("xpath=>//*[@id='timeWay']/option["+mydef.rad_num(1,3)+"]")

    #体验费用
    def charge(self):
        charge = mydef.rad_num(10,100)
        self.clear("id=>charge")
        self.type("id=>charge",charge)

    #体验费用说明
    def chargedesc(self):
        text = mydef.rad_word(10)
        self.clear("id=>chargedesc")
        self.type("id=>chargedesc",text)

    #请选择提供体验的房源
    def add_room(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[1]/dl/dd[7]/span[2]/img")

    #去掉全部房源
    def cancel_allroom(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[1]/div[1]/div[2]/div[2]/span[1]")

    #选择第一个房源
    def choose_oneroom(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[1]/div[1]/div[2]/div[2]/ul/li[1]/img")

    #确定
    def sure_add(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[1]/div[1]/div[2]/button")

    #提交审核
    def check(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div[1]/div[2]")

    #信息提交成功文案
    def success_text(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[3]/div[2]/p")
        return text

    #关闭弹窗
    def close_alert_windows(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[3]/div[2]/img")

    #完善个人资料
    def go_accountmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div/div[1]/div[3]/div[2]/div/a")

    #查看详情
    def look_des(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div[9]/div[2]/div[1]/div[3]/ul/li")


