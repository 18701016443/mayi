#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/21 20:42
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_accountmanager_page
from models import function,myunit
from time import sleep
import unittest

class TestAccountmanager(myunit.MyTest):
    '''房东个人信息'''

    def test_account(self):
        '''修改房东信息'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).accountmanager()
        sleep(1)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_accountmanager_page.LandlordAccountmanagerPage(self.driver)
        po.nickname()
        po.realname()
        sleep(2)
        po.paperno()
        po.sex()
        sleep(2)
        po.age()
        po.constellation()
        sleep(2)
        po.bloodtype()
        po.profession()
        sleep(2)
        po.saveuser()

if __name__ == "__main__":
    unittest.main()
