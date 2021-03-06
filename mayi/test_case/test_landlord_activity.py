#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 8:46
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_activity_page
from models import function,myunit
from time import sleep
import unittest

class TestActivity(myunit.MyTest):
    '''活动设置'''

    def test_active_good(self):
        '''活动好处'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).activitymanager()
        sleep(1)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_activity_page.LandlordActivity(self.driver)
        print(po.text())
        sleep(2)
        po.active_good()
        sleep(2)
        function.insert_img(self.driver,"activity_good.png")
        po.img_close()


    def test_regular_desc(self):
        '''活动规则'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).activitymanager()
        sleep(1)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_activity_page.LandlordActivity(self.driver)
        sleep(2)
        po.regular_desc()
        function.insert_img(self.driver,"regular_desc.png")
        print(po.regular_desc_text())
        po.regular_desc_close()

if __name__ == "__main__":
    unittest.main()