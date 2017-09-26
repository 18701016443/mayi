#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/19 13:43
"""
from .base import Pyse
from time import sleep

class LoginPage(Pyse):
    '''登录'''
    url = "/"
    #登录/注册
    def loginshow(self):
        self.click("xpath=>//*[@id='loginshow']")

    #账号密码登录
    def changeloginbyup(self):
        self.click("id=>changeloginbyup")

    #账号
    def username(self,username):
        self.type("id=>loginnamein",username)

    #密码
    def password(self,password):
        self.type("id=>loginpassin",password)

    #验证码
    def imagecode1(self):
        self.click("id=>imagecode1")
        sleep(8)

    #登录
    def loginbyupdo(self):
        self.click("id=>loginbyupdo")

    #登录成功返回文案
    def login_sucess(self):
        text = self.get_text("id=>head_nickname")
        return text

    def login(self):
        self.open()
        self.loginshow()
        self.changeloginbyup()
        self.username(username="18701016443")
        self.password(password="18701016443")
        self.imagecode1()
        self.loginbyupdo()
