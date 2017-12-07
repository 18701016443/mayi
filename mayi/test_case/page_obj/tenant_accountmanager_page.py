#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 14:50
"""
from .base import Pyse
from models import mydef

class TenantAccountManagePage(Pyse):
    '''房客账户管理'''

    #昵称
    def nickname(self):
        nickname = mydef.rad_word(5)
        self.clear("id=>nickname")
        self.type("id=>nickname",nickname)

    #真实姓名
    def realname(self):
        realname = mydef.rad_only_word(5)
        self.clear("id=>realname")
        self.type("id=>realname",realname)

    #性别
    def sex(self):
        self.click("xpath=>//*[@id='sex']/option["+mydef.rad_num(2,4)+"]")

    #邮箱
    def email(self):
        email = "757200708@qq.com"
        self.clear("id=>email")
        self.type("id=>email",email)

    #验证邮箱
    def validemail(self):
        self.click("xpath=>//*[@id='validemail']")

    #验证邮箱弹窗
    def sendemail(self):
        self.click("id=>sendemail")

    #验证邮箱文案
    def sendsuccess_text(self):
        text = self.get_text("xpath=>//*[@id='viewemaildiv']/div[2]/div[1]")
        return text

    #关闭邮箱验证弹窗
    def viewemaildivclose(self):
        self.click("id=>viewemaildivclose")

    #保存
    def saveuser(self):
        self.click("id=>saveuser")

####以下部分定位不成功
    # #保存成功
    # def save_success(self):
    #     self.click("xpath=>html/body/div[37]/div[1]/span/a")
    # #保存成功文案
    # def save_success_text(self):
    #     text = self.get_text("xpath=>html/body/div[37]/div[1]/h2/em")
    #     return text