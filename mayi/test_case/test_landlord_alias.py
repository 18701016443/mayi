#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 20:12
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_alias_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestAlias(myunit.MyTest):
    '''房源别名'''

    def test_alias(self):
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        po = landlord_alias_page.LandlordAliasPage(self.driver)
        po.alias()
        po.input_alias()
        function.insert_img(self.driver,"alias.png")

if __name__ == "__mian__":
    unittest.main()