#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/28 17:31
"""
from mayi.test_case.page_obj import mayi_QR_page
from mayi.models import jiexi_QR,myunit
from selenium import webdriver
from time import sleep
import unittest

class TestQR(myunit.MyTest):
    '''二维码解析'''

    def test_nav_QR(self):
        # driver = webdriver.Chrome()
        # driver.get("http://pre.mayi.com")
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.open()

        url = jiexi_QR.decode_qr(po.nav_qr())
        sleep(3)
        # driver.get(url)
        po.opentest(url)
        sleep(2)
        po.down_btn()
        sleep(2)
        self.driver.get("chrome://downloads/")
        sleep(2)
        text = po.text()
        sleep(2)
        text = text.split("\n")
        APP_name = text[5]
        APP_url = text[6]

        size = text[7].split("，")

        APP_size = size[1]
        sleep(2)
        print("")
        print("APP包名：" +APP_name)
        print("APP下载地址："+APP_url)
        print("APP大小："+APP_size)

if __name__ == "__main__":
    unittest.main()

