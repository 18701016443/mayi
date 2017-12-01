#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 9:21
"""

from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_microshopmanager_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestMicroshopManager(myunit.MyTest):
    '''房东微店'''

    def test_edit_weidian(self):
        '''编辑微店，更改微店名称和微店介绍'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).microshopmanager()

        po = landlord_microshopmanager_page.LandlordMicroshopManagerPage(self.driver)
        po.edit_weidian_btn()
        sleep(2)
        po.title()
        sleep(1)
        po.shop_introduction()
        sleep(2)
        function.insert_img(self.driver,"edit_weidian.png")
        po.save_edit_btn()


    def test_view_again(self):
        '''查看房东说明'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).microshopmanager()

        po = landlord_microshopmanager_page.LandlordMicroshopManagerPage(self.driver)
        po.view_again_btn()
        sleep(2)
        print(po.microshop_text())
        function.insert_img(self.driver,"view_weidian.png")



if __name__ == "__main__":
    unittest.main()