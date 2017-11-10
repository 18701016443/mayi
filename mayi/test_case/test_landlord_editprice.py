#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 15:36
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,fabu_room_page,landlord_editprice_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestLandlordEditprice(myunit.MyTest):
    '''审核中-修改价格'''
    def test_editprice(self):
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_editprice_page.LandlordEditpricePage(self.driver)
        fb = fabu_room_page.FabuRoomPage(self.driver)

        po.roomfilter2()
        sleep(2)
        po.edit_price()
        sleep(2)
        fb.dayprice()
        sleep(2)
        fb.weekendtype()
        sleep(2)
        fb.weekpriceRet()
        sleep(2)
        fb.monthpriceRet()
        sleep(2)
        po.specialdiscount_yes()
        sleep(2)
        function.insert_img(self.driver,"editPrice.png")
        po.confirmModifyPriceBtn()

        print(po.editsuccess_text())
        assert po.editsuccess_text()=="修改成功！"
        po.changePriceSuccessBtn()

if __name__ == "__main__":
    unittest.main()
