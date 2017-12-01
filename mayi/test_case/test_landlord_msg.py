#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 16:38
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_msg_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestLandlordMsg(myunit.MyTest):
    '''消息回复'''
    def test_msg(self):
        '''房东回复房客'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).msgmanager()

        po = landlord_msg_page.LandlordMsgPage(self.driver)
        po.return_msg()
        sleep(2)
        po.IM_text()
        po.send_msg()
        sleep(2)
        function.insert_img(self.driver,"IM_msg.png")
        po.shrink()


    def test_msg_record(self):
        '''打印聊天记录'''
        # login_page.LoginPage(self.driver).login()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        # landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        # sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).msgmanager()

        po = landlord_msg_page.LandlordMsgPage(self.driver)
        po.look()
        print(po.msg_record())
        function.insert_img(self.driver,"msg_record.png")

if __name__ == "__main__":
    unittest.main()