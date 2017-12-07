#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 20:48
"""
from models import myunit,function
from test_case.page_obj import landlord_serach_page,landlord_nav_page,login_page
import unittest
from time import sleep

class TestLandlordSerach(myunit.MyTest):
    '''搜索'''
    def test_date_serach(self):
        '''按日期搜索'''
        login_page.LoginPage(self.driver).login()
        sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(4)
        po = landlord_serach_page.LandlordSerachPage(self.driver)
        po.beginCheckInDay()
        po.endCheckInDay()
        sleep(2)
        po.serach()
        sleep(3)
        function.insert_img(self.driver,"date_serach.png")

    def test_orderid_or_phone(self):
        '''按手机号或订单号搜索'''
        # login_page.LoginPage(self.driver).login()
        # sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(4)
        po = landlord_serach_page.LandlordSerachPage(self.driver)
        list = ["18701016443","853519722 "]
        for orderOrMoblie in list:
            po.orderOrMoblie(orderOrMoblie)
            sleep(2)
            po.serach()
            function.insert_img(self.driver,orderOrMoblie+".png")

if __name__ == "__main__":
    unittest.main()


