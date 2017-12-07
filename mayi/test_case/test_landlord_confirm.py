#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 11:17
"""
from time import sleep
from models import myunit,function
from test_case.page_obj import login_page,landlord_nav_page,landlord_confirm_page
import unittest

class TestLandlordConfiem(myunit.MyTest):
    '''待确认订单'''

    def test_confirm(self):
        '''②确认订单'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.confirm_btn()
        sleep(2)
        po.alert_confirm()
        sleep(2)
        #确认订单后应和数据库的状态作对比，以后再维护


    def test_cancel(self):
        '''①确认订单-以后再说'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.confirm_btn()
        sleep(2)
        po.cancel()


    def test_refuse(self):
        '''⑤拒绝订单'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.refuse()
        po.refuse_reason()
        sleep(2)
        po.refuse_order()

    def test_refuse_cancel(self):
        '''⑥拒绝-取消按钮'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.refuse()
        sleep(2)
        po.refuse_cancel()

    def test_return_myorder(self):
        '''⑦订单详情页-返回我的订单'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.order_details()
        sleep(2)
        po.return_myorder()


    def test_order_details_confirm(self):
        '''③订单详情页-确认订单'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.order_details()
        sleep(1)
        po.order_details_confirm()
        sleep(1)
        po.alert_order_details_confirm()

    def test_order_details_refuse(self):
        '''④订单详情页-拒绝'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_confirm_page.LandlordConfirmPage(self.driver)
        po.confirm()
        po.order_details()
        sleep(1)
        po.order_details_refuse()
        sleep(1)
        po.alert_details_refuse_reason()
        sleep(1)
        po.alert_details_refuse_order()

if __name__ == "__main__":
    unittest.main()