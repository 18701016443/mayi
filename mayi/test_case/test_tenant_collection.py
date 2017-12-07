#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/27 14:08
"""
from test_case.page_obj import login_page,tenant_nav_page,tenant_collection_page
from models import myunit,function
from time import sleep
import unittest

class TestTenantCollection(myunit.MyTest):
    '''我的收藏'''

    def test_a_collection(self):
        '''五家渠收藏房源'''

        login_page.LoginPage( self.driver ).login()
        sleep( 2 )
        login_page.LoginPage( self.driver )._open( url="/wujiaqu/" )
        sleep( 2 )

        po = tenant_collection_page.TenantCollectionPage( self.driver )
        if po.title()=="收藏":
            po.collection()
        else:
            po.collection()
            sleep(2)
            po.collection()
        function.insert_img( self.driver, "collection.png" )

    def test_cancel_collection(self):
        '''我的收藏——取消收藏'''

        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).Iamtenant()
        sleep(3)
        tenant_nav_page.TenantNavPage(self.driver).mycollection()

        po = tenant_collection_page.TenantCollectionPage(self.driver)
        sleep(3)


        try:
            po.cancel_collection()
            sleep(2)
            function.insert_img(self.driver,"cancel_collection.png")
        except :
            print("没有收藏房源")


if __name__ == "__main__":
    unittest.main()

