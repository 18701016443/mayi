#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 11:03
"""
from test_case.page_obj import login_page,landlord_nav_page,landlord_online_editdata,fabu_room_page
from models import myunit,function
from time import sleep
import unittest

class TestLandlordOnlineEditdata(myunit.MyTest):
    '''已上线——房源信息'''

    def test_edit_fydes(self):
        '''修改房源信息'''
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).roommanager()

        po = landlord_online_editdata.LandlordOnlineEditdata(self.driver)
        fb = fabu_room_page.FabuRoomPage(self.driver)
        po.editdata()
        sleep(2)
        po.div_is_13or15()

        sleep(2)
        # po.room_type(div)
        po.dixiashi()
        sleep(2)
        fb.roomnum()
        sleep(2)
        fb.parlor()
        sleep(2)
        fb.cookhouse()
        fb.balcony()
        sleep(2)
        fb.privatetoiletnum()
        po.js("var j = document.body.scrollTop=500")
        sleep(2)
        po.sheet_replacement()
        sleep(2)
        po.save()
        print(po.editsuccess_text())
        assert po.editsuccess_text()=="已提交，我们会在1-2个工作日内审核完毕！"
        po.auditLodgeConfirmBtn()

if __name__ == "__main__":
    unittest.main()
