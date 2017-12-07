#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/26 14:31
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_read_page
from models import function,myunit
from time import sleep
import unittest

class TestLandlordRead(myunit.MyTest):
    '''房源管理-房东必读'''

    def test_agreement(self):
        '''服务协议'''
        login_page.LoginPage(self.driver).login()
        sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(3)

        po = landlord_read_page.LandlordReadPage(self.driver)
        po.read()
        sleep(3)
        po.agreement()
        print(po.agreement_text())
        sleep(2)
        function.insert_img(self.driver, "agreement.png")

    def test_landlord_read(self):
        '''房东规则'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(2)

        po = landlord_read_page.LandlordReadPage(self.driver)
        po.read()
        sleep(2)
        function.insert_img(self.driver,"landlord_read.png")

    def test_tenant_rule(self):
        '''房客规则'''
        # login_page.LoginPage(self.driver).login()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(3)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(3)

        po = landlord_read_page.LandlordReadPage(self.driver)
        po.read()
        sleep(3)
        po.tenant_rule()
        function.insert_img(self.driver,"tenant_rule.png")


    def test_roomauditrule(self):
        '''房间审核规范'''
        # login_page.LoginPage(self.driver).login()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(3)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(3)

        po = landlord_read_page.LandlordReadPage(self.driver)
        po.read()
        sleep(3)
        po.roomauditrule()
        function.insert_img(self.driver, "roomauditrule.png")


    def test_privacypolicy(self):
        '''隐私条款'''
        # login_page.LoginPage(self.driver).login()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(3)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(3)

        po = landlord_read_page.LandlordReadPage(self.driver)
        po.read()
        sleep(3)
        po.privacypolicy()
        print(po.privacypolicy_text())
        function.insert_img(self.driver, "privacypolicy.png")

    def test_disclaimer(self):
        '''免责声明'''
        # login_page.LoginPage(self.driver).login()
        # sleep(3)
        landlord_nav_page.LandlordNavPage( self.driver ).Iamlandlord()
        sleep( 3 )
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(3)
        landlord_nav_page.LandlordNavPage( self.driver ).roommanager()
        sleep( 3 )

        po = landlord_read_page.LandlordReadPage( self.driver )
        po.read()
        sleep( 3 )
        po.disclaimer()
        print( po.disclaimer_text() )
        function.insert_img( self.driver, "disclaimer.png" )


if __name__ == "__main__":
    unittest.main()
