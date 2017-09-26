#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 14:54
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,fabu_room_page,landlord_online_editdata
from mayi.models import myunit,function
from time import sleep
import unittest,os

class TestEditdataFypic(myunit.MyTest):
    '''房源图片'''

    def test_setcover(self):
        '''设为封面'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_online_editdata.LandlordOnlineEditdata(self.driver)
        po.editdata()
        sleep(2)
        po.fy_picture()
        sleep(2)
        po.setcover()
        function.insert_img(self.driver,"setcover.png")
        po.pic_save()

    def test_del_pic(self):
        '''修改房源图片——上传图片和删除图片'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_online_editdata.LandlordOnlineEditdata(self.driver)
        po.editdata()
        sleep(2)
        po.fy_picture()
        sleep(2)
        po.del_pic()
        sleep(2)
        po.SWFUpload_0()
        sleep(3)
        os.system("D:/python/mayi/data/up.exe")
        sleep(2)
        function.insert_img(self.driver,"del_up_pic.png")
        po.pic_save()


if __name__ == "__main__":
    unittest.main()
