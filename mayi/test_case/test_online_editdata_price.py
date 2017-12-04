#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 15:17
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_online_editdata,fabu_room_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestEditPrice(myunit.MyTest):
    '''价格要求'''

    def test_price(self):
        '''修改房源价格'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_online_editdata.LandlordOnlineEditdata(self.driver)
        fb = fabu_room_page.FabuRoomPage(self.driver)

        po.editdata()
        sleep(2)
        po.fy_price()

        fb.dayprice()
        sleep(2)
        fb.weekendtype()
        sleep(2)
        fb.weekpriceRet()
        sleep(2)
        fb.addbed()
        fb.addbed_more()
        sleep(2)
        fb.cook()
        sleep(2)
        fb.upto()

        po.price_save()
        print( po.editsuccess_text() )
        sleep(2)
        function.insert_img(self.driver,"test_price.png")
        po.auditLodgeConfirmBtn()


if __name__ == "__main__":
    unittest.main()
