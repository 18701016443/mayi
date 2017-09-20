#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 17:31
"""
from mayi.test_case.page_obj import wujiaqu_order_page
from mayi.models import function,myunit
from time import  sleep
from mayi.test_case.test_login import TestLogin
import unittest

class TestWujiaquOrder(myunit.MyTest):
    '''五家渠下订单'''

    def test_wujiaqu_order(self):
        po  = wujiaqu_order_page.WujiaquOrderPage(self.driver)
        TestLogin.test_login(self)
        po._open(url="/wujiaqu/")

        po.searchcityin1()
        po.landmarkBtn()
        po.one_room()
        sleep(3)
        po.goBookBtn()
        sleep(2)
        po.people()
        sleep(1)
        po.tenantname()
        sleep(1)
        po.user()
        sleep(1)
        po.submit_order()
        sleep(2)
        print(po.order_success())
        assert po.order_success()=="订单提交成功"
        function.insert_img(self.driver,"order_success.png")



if __name__ == "__main__":
    unittest.main()