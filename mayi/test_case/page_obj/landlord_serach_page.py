#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 20:30
"""
from .base import Pyse
from .landlord_nav_page import LandlordNavPage
import datetime

class LandlordSerachPage(Pyse):
    '''房东订单搜索'''

    url = "/"

    #入住开始时间
    def beginCheckInDay(self):
        self.js("document.getElementById('beginCheckInDay').readOnly=false;")
        beginCheckInDay =datetime.datetime.now().strftime("%Y-%m-%d")
        self.type("id=>beginCheckInDay",beginCheckInDay)

    #入住结束时间
    def endCheckInDay(self):
        self.js("document.getElementById('endCheckInDay').readOnly=false;")
        endCheckInDay =(datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.type("id=>endCheckInDay",endCheckInDay)


    #按订单号或手机号
    def orderOrMoblie(self,orderOrMoblie):
        self.clear("id=>orderOrMoblie")
        self.type("id=>orderOrMoblie",orderOrMoblie)

    #搜索
    def serach(self):
        self.click("xpath=>/html/body/div[13]/div[5]/div/div[1]/div[2]/input[2]")