#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 16:33
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_microshop_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestMicroshop(myunit.MyTest):
    '''微店订单'''

    def test_microshop_status(self):
        '''进入订单详情页并打印状态'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_microshop_page.LandlordMicroshopPage(self.driver)
        po.microshop()
        po.microshop_order_details()
        print(po.microshop_order_details_status())
        function.insert_img(self.driver,"microshop_orderdetails_status.png")

    def test_microshop_return_myorder(self):
        '''返回我的订单并打印第一个状态'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_microshop_page.LandlordMicroshopPage(self.driver)
        po.microshop()
        po.microshop_order_details()
        po.microshop_return_myorder()
        print(po.status())
        function.insert_img(self.driver,"microshop_return_myorder.png")

if __name__ == "__main__":
    unittest.main()