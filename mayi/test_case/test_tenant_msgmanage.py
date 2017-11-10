#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 14:42
"""
from mayi.test_case.page_obj import login_page,tenant_nav_page,tenant_msgmanage_page,landlord_msg_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestTenantMsg(myunit.MyTest):
    '''房客消息通知'''

    def test_tenant_msg(self):
        '''房客消息通知'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).Iamtenant()
        sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).msgmanager()

        po = tenant_msgmanage_page.TenantMsganagePage(self.driver)
        po.return_msg()
        sleep(2)
        lm = landlord_msg_page.LandlordMsgPage(self.driver)
        lm.IM_text()

        lm.send_msg()
        sleep(3)
        function.insert_img(self.driver,"tenant_msg.png")
        lm.shrink()

if __name__ == "__main__":
    unittest.main()

