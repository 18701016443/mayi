#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:52
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_manageStandard_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestManageStandard(myunit.MyTest):
    '''管理规范'''

    def test_managestandard(self):
        '''管理规范的文案及截图'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).manageStandard()

        po = landlord_manageStandard_page.LandlordManageStandardPage(self.driver)
        print(po.manageStandard_text())
        function.insert_img(self.driver,"managestandard.png")

if __name__ == "__main__":
    unittest.main()
