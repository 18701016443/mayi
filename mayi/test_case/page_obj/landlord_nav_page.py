#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 20:14
"""
from .base import Pyse

class LandlordNavPage(Pyse):
    '''房东导航集'''
    url = "/"

    #我是房东
    def Iamlandlord(self):
        self.click("xpath=>/html/body/div[1]/div/ul/li[3]/div/a")

    #房东微信
    def close_weiChat(self):
        self.click("xpath=>/html/body/div[14]/div[2]/div[2]/img[1]")

    #房源管理
    def roommanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[2]/a")

    #消息通知
    def msgmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[3]/a")

    #结算管理
    def settlements(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[4]/a")

    #房东微店
    def microshopmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[5]/a")

    #特色体验
    def experience(self):
        self.click("xpath=>//*[@id='experience']/a")

    #房东微信
    def landlordweixin(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[7]/a")

    #房东讲堂
    def forum(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[8]/a")

    #管理规范
    def manageStandard(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[9]/a")

    #身份验证
    def authentication(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[10]/a")

    #个人信息
    def accountmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[11]/div/a[1]")

    #收款设置
    def paymentmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[11]/div/a[2]")

    #密码设置
    def passwordmanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[11]/div/a[3]")

    #活动设置
    def activitymanager(self):
        self.click("xpath=>/html/body/div[14]/div[5]/ul/li[11]/div/a[4]")