#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 20:23
"""
from .base import Pyse
from models import mydef

class LandlordAccountmanagerPage(Pyse):
    '''房东个人信息'''

    #昵称：
    def nickname(self):
        nickname = mydef.rad_word(5)
        self.clear("id=>nickname")
        self.type("id=>nickname",nickname)

    #真实姓名
    def realname(self):
        realname = mydef.rad_only_word(5)
        self.clear("id=>realname")
        self.type("id=>realname",realname)

    #证件类型.papertype传参用于判断是否选择国家地区
    def papertype(self,papertype):
        self.click("xpath=>//*[@id='papertype']/option["+papertype+"]")

    #国家/地区
    def country(self):
        self.click("xpath=>//*[@id='country']/option["+mydef.rad_num(2,200)+"]")

    #证件号码
    def paperno(self):
        paperno = mydef.rad_num(100,9999)
        self.type("id=>paperno",paperno)

    #性别
    def sex(self):
        self.click("xpath=>//*[@id='sex']/option["+mydef.rad_num(2,4)+"]")

    #年龄
    def age(self):
        self.click("xpath=>//*[@id='age']/option["+mydef.rad_num(2,7)+"]")

    #星座
    def constellation(self):
        self.click("xpath=>//*[@id='constellation']/option["+mydef.rad_num(2,13)+"]")

    #血型
    def bloodtype(self):
        self.click("xpath=>//*[@id='bloodtype']/option["+mydef.rad_num(2,6)+"]")

    #故乡
    def housetownprov(self):
        self.click("xpath=>//*[@id='housetownprov']/option[1]")

    def housetowncity(self):
        self.click("xpath=>//*[@id='housetowncity']/option")

    #职业
    def profession(self):
        profession = mydef.rad_word(5)
        self.clear("id=>profession")
        self.type("id=>profession",profession)

    #房东简介
    def introduce(self):
        introduce = mydef.rad_word(20)
        self.type("id=>introduce",introduce)

    #保存
    def saveuser(self):
        self.click("xpath=>//*[@id='saveuser']")