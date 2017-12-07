#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 16:16
"""
from models import function,myunit
from test_case.page_obj import login_page,landlord_nav_page,landlord_invalid_page
from time import sleep
import unittest

class TestInvalid(myunit.MyTest):
    '''失效订单'''
    def test_order_status(self):
        '''进入订单详情页并打印状态'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_invalid_page.LandlordInvalidPage(self.driver)
        po.invalid()
        po.invalid_order_details()
        print(po.invalid_order_details_status())
        function.insert_img(self.driver, "invalid_orderdetails_status.png")

    def test_return_myorder(self):
        '''返回我的订单并打印第一个订单的状态'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po = landlord_invalid_page.LandlordInvalidPage(self.driver)
        po.invalid()
        po.invalid_order_details()
        po.invalid_return_my_order()
        print(po.status())
        function.insert_img(self.driver, "invalid_refund_order.png")

if __name__ == "__main__":
    unittest.main()