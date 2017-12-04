#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 11:02
"""
from .base import Pyse

class TenantNavPage(Pyse):
    '''房客导航'''

    #我是房客
    def Iamtenant(self):
        self.click("id=>head_nickname")

    #消息通知
    def msgmanager(self):
        self.click("xpath=>html/body/div[14]/div[1]/ul/li[2]/a")

    #账号管理
    def accountmanager(self):
        self.click("xpath=>html/body/div[14]/div[1]/ul/li[3]/a")

    #我的收藏
    def mycollection(self):
        self.click("xpath=>/html/body/div[14]/div[1]/ul/li[4]/a")