#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 14:15
"""
from mayi.test_case.page_obj import login_page,tenant_nav_page,tenant_againorder_page,wujiaqu_order_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestAgainOrder(myunit.MyTest):
    '''房客重新下单'''
    def test_againorder(self):
        '''重新下单'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        tenant_nav_page.TenantNavPage(self.driver).Iamtenant()

        po = tenant_againorder_page.TenantAgainorderPage(self.driver)
        po.againorder()
        po._open(url="/room/851272901")

        sleep(2)
        wo = wujiaqu_order_page.WujiaquOrderPage(self.driver)
        wo.goBookBtn()
        sleep(2)
        wo.people()
        wo.tenantname()
        sleep(2)
        wo.user()
        wo.submit_order()
        sleep(2)
        print(wo.order_success())
        assert wo.order_success()=="订单提交成功"
        function.insert_img(self.driver, "againorder_success.png")

if __name__ == "__main__":
    unittest.main()