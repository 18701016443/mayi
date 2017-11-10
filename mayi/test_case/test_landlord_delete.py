#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 10:08
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_delete_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestDelete(myunit.MyTest):
    '''房源删除'''

    def test_room_delete(self):
        '''已上线——删除房源'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_delete_page.LandlordDeletePage(self.driver)
        po.room_delete()
        sleep(1)
        po.delBtn()
        sleep(2)
        print(po.delsuccess_text())
        assert po.delsuccess_text()=="删除成功！"
        function.insert_img(self.driver,"delete.png")
        po.okDelSuccessBtn()

    def test_offlineroom_delete(self):
        '''已下线——删除房源'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_delete_page.LandlordDeletePage(self.driver)
        po.roomfilter5()
        po.room_delete()
        sleep(1)
        po.delBtn()
        sleep(2)
        print(po.delsuccess_text())
        assert po.delsuccess_text()=="删除成功！"
        function.insert_img(self.driver,"delete.png")
        po.okDelSuccessBtn()

    def test_checkingroom_delete(self):
        '''审核中——删除房源'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()
        sleep(2)
        po = landlord_delete_page.LandlordDeletePage(self.driver)
        po.roomfilter2()
        sleep(2)
        po.checking_delete()
        sleep(1)
        po.delBtn()
        sleep(2)
        print(po.delsuccess_text())
        assert po.delsuccess_text()=="删除成功！"
        function.insert_img(self.driver,"delete.png")
        po.okDelSuccessBtn()


    def test_nopassroom_delete(self):
        '''未通过——删除房源'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_delete_page.LandlordDeletePage(self.driver)
        po.roomfilter3()
        po.checking_delete()
        sleep(1)
        po.delBtn()
        sleep(2)
        print(po.delsuccess_text())
        assert po.delsuccess_text()=="删除成功！"
        function.insert_img(self.driver,"delete.png")
        po.okDelSuccessBtn()

    def test_need_complete_delete(self):
        '''待完善——删除房源'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_delete_page.LandlordDeletePage(self.driver)
        po.roomfilter1()
        po.need_complete_delete()
        sleep(1)
        po.delBtn()
        sleep(2)
        print(po.delsuccess_text())
        assert po.delsuccess_text()=="删除成功！"
        function.insert_img(self.driver,"delete.png")
        po.okDelSuccessBtn()



if __name__ == "__main__":
    unittest.main()