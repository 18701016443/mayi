#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 15:02
"""
from test_case.page_obj import login_page,tenant_nav_page,tenant_accountmanager_page
from models import function,myunit
from time import sleep
import unittest

class TestTenantAccount(myunit.MyTest):
    '''房客个人信息'''
    def test_tenant_account(self):
        '''房客个人信息'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).Iamtenant()
        sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).accountmanager()

        po = tenant_accountmanager_page.TenantAccountManagePage(self.driver)
        po.nickname()
        sleep(2)
        po.realname()
        po.sex()
        sleep(2)
        # po.email()
        # po.validemail()
        # sleep(2)
        # po.sendemail()
        # print(po.sendsuccess_text())
        # sleep(5)
        # function.insert_img(self.driver,"send_email.png")
        # po.viewemaildivclose()
        # sleep(60)

        po.saveuser()
        sleep(2)
        # print(po.save_success_text())
        # assert po.save_success_text()=="保存成功"
        function.insert_img(self.driver,"tenant_account.png")
        # po.save_success()


if __name__ == "__main__":
    unittest.main()