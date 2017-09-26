#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:44
"""

from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_forum_page
from mayi.models import myunit,function
from time import sleep
import unittest

class TestForum(myunit.MyTest):
    '''房东讲堂'''

    def test_forum(self):
        '''房东讲堂文案及截图'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).forum()

        po = landlord_forum_page.LandlordForumPage(self.driver)
        print(po.forum_text())
        function.insert_img(self.driver,"forum.png")

if __name__ == "__main__":
    unittest.main()
