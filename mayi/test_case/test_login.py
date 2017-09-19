#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/19 14:17
"""
import unittest,sys
from mayi.test_case.page_obj import login_page
from mayi.models import myunit,function
from time import sleep


class TestLogin(myunit.MyTest):
    '''登录'''
    def test_login(self):
        po = login_page.LoginPage(self.driver)
        po.open()
        po.loginshow()
        po.changeloginbyup()
        po.username(username="18701016443")
        po.password(password="18701016443")
        po.imagecode1()
        po.loginbyupdo()
        sleep(3)

        assert po.login_sucess() == "哈哈哈哈哈"
        function.insert_img(self.driver, "login.png")

        print(po.login_sucess())
        sleep(3)

if __name__ == "__main__":
    unittest.main()

