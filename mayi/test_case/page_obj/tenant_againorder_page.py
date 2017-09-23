#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 11:09
"""
from .base import Pyse

class TenantAgainorderPage(Pyse):
    '''房客重新下订单'''

    #重新下定单
    def againorder(self):
        self.click("xpath=>/html/body/div[13]/div[1]/div/div[1]/div/div[4]/div[2]/div[6]/p/a")





