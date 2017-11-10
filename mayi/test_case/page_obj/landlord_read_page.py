#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/26 14:18
"""

from .base import Pyse

class LandlordReadPage(Pyse):
    '''房源管理——房东必读'''

    #房东必读
    def read(self):
        self.open_new_window("class=>bidu")

    #房客规则
    def tenant_rule(self):
        self.click("xpath=>/html/body/ul/li[2]/a")

    #房间审核规范
    def roomauditrule(self):
        self.click("xpath=>/html/body/ul/li[3]/a")

    #服务协议
    def agreement(self):
        self.click("xpath=>/html/body/ul/li[4]/a")

    #服务器协议文案
    def agreement_text(self):
        text = self.get_text("xpath=>/html/body/div[14]")
        return text

    #隐私条款
    def privacypolicy(self):
        self.click("xpath=>/html/body/ul/li[5]/a")


