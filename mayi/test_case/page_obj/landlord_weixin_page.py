#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:31
"""
from .base import Pyse

class LandlordWeixinPage(Pyse):
    '''房东微信'''

    #房东微信文案
    def weixin_text(self):
        text = self.get_text("xpath=>/html/body/div[13]/div[5]/div/h3")
        return text
