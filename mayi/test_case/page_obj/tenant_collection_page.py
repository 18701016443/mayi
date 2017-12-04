#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/27 10:49
"""
from .base import Pyse

class TenantCollectionPage(Pyse):
    '''房客收藏'''

    #收藏按钮
    def collection(self):
        self.click("xpath=>html/body/div[15]/div[1]/div[2]/div[2]/div/dl/dd[1]/div/div[1]")

    def title(self):
        title = self.get_attribute("xpath=>html/body/div[15]/div[1]/div[2]/div[2]/div/dl/dd[1]/div/div[1]","title")
        return title


    #获得收藏房源的ID
    def collection_ID(self):
        e = self.get_element("xpath=>html/body/div[6]/div[1]/div[2]/div[2]/div/dl/dd[1]/div/div[1]")
        id = e.get_attribute("id")
        id = id.split("_")[1]
        return id

    #我的收藏——取消收藏
    def cancel_collection(self):
        self.click("xpath=>html/body/div[14]/div/div/div/div/div[1]/div[2]/p[2]/font")

