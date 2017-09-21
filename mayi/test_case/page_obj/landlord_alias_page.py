#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 20:07
"""
from .base import Pyse
from mayi.models import mydef

class LandlordAliasPage(Pyse):
    '''房源管理-设置别名'''
    url = "/"

    #设置别名
    def alias(self):
        self.click("xpath=>html/body/div[13]/div[5]/div/div/div[1]/div[1]/div[2]/div[3]/p[2]/input")

    #输入别名
    def input_alias(self):
        alias = mydef.rad_word(5)
        self.clear("xpath=>html/body/div[13]/div[5]/div/div/div[1]/div[1]/div[2]/div[3]/p[1]/input")
        self.type("xpath=>html/body/div[13]/div[5]/div/div/div[1]/div[1]/div[2]/div[3]/p[1]/input",alias)


