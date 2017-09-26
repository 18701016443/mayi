#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 10:24
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_online_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestOnline(myunit.MyTest):
    '''已下线-房源上线'''

    def test_room_online(self):
        '''房源上线'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_online_page.LandlordOnlinePage(self.driver)

        po.roomfilter5()
        sleep(2)
        po.room_online()
        sleep(2)
        print(po.onlinesuccess_text())
        assert po.onlinesuccess_text()=="上线成功！"
        sleep(2)
        po.onlineSuccessBtn()

if __name__ == "__main__":
    unittest.main()