#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:41
"""

from .base import Pyse

class LandlordForumPage(Pyse):
    '''房东讲堂'''

    #房东讲堂文案
    def forum_text(self):
        text = self.get_text("xpath=>/html/body/div[13]/div[5]/div")
        return text
