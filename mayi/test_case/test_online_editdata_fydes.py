#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 14:21
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,fabu_room_page,landlord_online_editdata
from mayi.models import myunit
from time import sleep
import unittest

class TestEditdataFydes(myunit.MyTest):
    '''修改房源'''

    def test_edit_fy_des(self):
        '''修改房源描述'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        fb = fabu_room_page.FabuRoomPage(self.driver)

        po = landlord_online_editdata.LandlordOnlineEditdata(self.driver)

        po.editdata()
        po.fy_des()
        po.is_element_exist("xpath=>html/body/div[14]/div[2]/div/div/div[2]/form/div[1]/p/em")
        sleep(2)

        #之前的逻辑是修改地理位置，后来逻辑改为不可修改地理位置，因此注释以下代码
        # po.EditAddress()
        # sleep(2)
        # po.changePosition()


        sleep(1)
        fb.title()
        fb.intro()
        sleep(2)
        fb.landmark()
        fb.traffic()
        sleep(2)
        fb.surroundings()
        fb.userule()
        sleep(2)
        fb.otherintro()
        sleep(2)
        po.fydes_save()
        print(po.editsuccess_text())
        po.auditLodgeConfirmBtn()

if __name__ == "__main__":
    unittest.main()
