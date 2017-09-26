#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 17:11
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_roomsearch_page
from mayi.models import function,myunit,mydef
from time import sleep
import unittest

class TestRoomsearch(myunit.MyTest):
    '''结算管理'''
    def test_roomsearch(self):
        '''按房间名搜索'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).settlements()

        po = landlord_roomsearch_page.LandlordRoomsearchPage(self.driver)
        num = mydef.rad_num(2,3)
        po.lodgeunitid(num)
        sleep(1)
        po.search()

if __name__ == "__main__":
    unittest.main()