#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 9:28
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_offline_page
from models import function,myunit,mydef
from time import sleep
import unittest

class TestOffline(myunit.MyTest):
    '''房源下线'''

    def test_gopriceCal(self):
        '''房源下线（去价格房态）——下线原因：我想休息，暂停出租'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_offline_page.LandlordOfflinePage(self.driver)
        po.room_offline()
        num = 1
        po.offline_reason(str(num))
        sleep(2)
        po.offlineReasonBtn()
        sleep(1)
        po.gopriceCal()
        sleep(2)
        function.insert_img(self.driver,"gopriceCal.png")

    def test_room_offline(self):
        '''房源下线——下线原因：非我想休息，暂停出租'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_offline_page.LandlordOfflinePage(self.driver)
        po.room_offline()
        num = mydef.rad_num(2,9)
        po.offline_reason(num)
        sleep(2)
        po.offlineReasonBtn()
        function.insert_img(self.driver,"offlineSuccess.png")
        print(po.offlineSuccess_text())
        sleep(2)
        po.okOfflineSuccessBtn()

    def test_offline(self):
        '''房源下线——下线原因：我想休息，暂停出租'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_offline_page.LandlordOfflinePage(self.driver)
        po.room_offline()
        num = 1
        po.offline_reason(str(num))
        po.offlineReasonBtn()
        sleep(2)
        function.insert_img(self.driver,"offline.png")
        po.offlineBtn()
        print(po.offlineSuccess_text())
        sleep(2)
        assert po.offlineSuccess_text()=="下线成功！"
        po.okOfflineSuccessBtn()


if __name__ == "__main__":
    unittest.main()
