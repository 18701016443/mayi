#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:50
"""
from .base import Pyse

class LandlordManageStandardPage(Pyse):
    '''管理规范'''

    #管理规范的文案
    def manageStandard_text(self):
        text = self.get_text("xpath=>/html/body/div[13]/div[3]/div/div/div[2]")
        return text
