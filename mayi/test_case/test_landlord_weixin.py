#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:34
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_weixin_page
from models import myunit,function
from time import sleep
import unittest

class TestWeixin(myunit.MyTest):
    '''房东微信'''
    def test_weixin(self):
        '''房东微信'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).landlordweixin()
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_weixin_page.LandlordWeixinPage(self.driver)
        print(po.weixin_text())
        function.insert_img(self.driver,"landloed_weixin.png")

if __name__ == "__main__":
    unittest.main()

