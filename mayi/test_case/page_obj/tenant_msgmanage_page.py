#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 14:36
"""

from .base import Pyse

class TenantMsganagePage(Pyse):
    '''房客消息通知'''

    #回复
    def return_msg(self):
        self.click("xpath=>html/body/div[13]/div/div/div/div/div[1]/div[2]/ul/li[2]/span/span/a")

    # 查看
    def look(self):
        self.click("xpath=>html/body/div[13]/div/div/div/div/div[1]/div[2]/ul/li[1]/a")


