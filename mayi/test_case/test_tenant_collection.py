#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/27 14:08
"""
from mayi.test_case.page_obj import login_page,tenant_nav_page,tenant_collection_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestTenantCollection(myunit.MyTest):
    '''我的收藏'''

    def test_cancel_collection(self):
        '''我的收藏——取消收藏'''
        try:
            login_page.LoginPage(self.driver).login()
            sleep(2)
            tenant_nav_page.TenantNavPage(self.driver).Iamtenant()
            sleep(3)
            tenant_nav_page.TenantNavPage(self.driver).mycollection()

            po = tenant_collection_page.TenantCollectionPage(self.driver)
            sleep(3)
            po.cancel_collection()
            sleep(2)
            function.insert_img(self.driver,"cancel_collection.png")
        except :
            tenant_collection_page.TenantCollectionPage(self.driver).accept_alert()


    def test_collection(self):
        '''五家渠收藏房源'''
        try:
            login_page.LoginPage(self.driver).login()
            sleep(2)
            login_page.LoginPage(self.driver)._open(url="/wujiaqu/")
            sleep(2)

            po = tenant_collection_page.TenantCollectionPage(self.driver)
            po.collection()
            function.insert_img(self.driver,"collection.png")
        except:
            tenant_collection_page.TenantCollectionPage(self.driver).accept_alert()


if __name__ == "__main__":
    unittest.main()
