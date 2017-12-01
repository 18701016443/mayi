#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 15:22
"""
from mayi.models import myunit,function
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_waitingcheckin_page
from time import sleep
import unittest

class TestWaitingcheckin(myunit.MyTest):
    '''待入住订单'''

    def test_return_myorder(self):
        '''从订单详情页返回到我的订单列表'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_waitingcheckin_page.LandlordWaitingcheckinPage(self.driver)
        po.waitingcheckin()
        po.wait_order_details()
        po.wait_return_my_order()
        print(po.status())
        assert po.status()=="待入住"
        function.insert_img(self.driver,"myorder.png")

    def test_status(self):
        '''进入订单详情页的并打印状态'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_waitingcheckin_page.LandlordWaitingcheckinPage(self.driver)
        po.waitingcheckin()
        po.wait_order_details()
        print(po.wait_order_details_status())
        assert po.wait_order_details_status()=="待入住"
        function.insert_img(self.driver,"wait_order_status.png")



if __name__ == "__main__":
    unittest.main()