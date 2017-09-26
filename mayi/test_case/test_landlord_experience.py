#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 10:08
"""
from mayi.test_case.page_obj import login_page,landlord_nav_page,landlord_experience_page,fabu_room_page
from mayi.models import function,myunit
from time import sleep
import unittest

class TestExperience(myunit.MyTest):
    '''特色体验'''

    def test_new_tsty(self):
        login_page.LoginPage(self.driver).login()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).experience()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()

        po = landlord_experience_page.LandlordExperiencePage(self.driver)
        po.new_tsty()
        sleep(2)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()
        po.title()
        po.introduction()
        sleep(2)
        po.details()
        po.experiencehour()
        sleep(2)
        po.timeWay()
        po.charge()
        sleep(2)
        po.chargedesc()
        po.add_room()
        sleep(2)
        po.cancel_allroom()
        po.choose_oneroom()
        sleep(2)
        po.sure_add()

        fabu_room_page.FabuRoomPage(self.driver).up_picture()
        sleep(2)

        po.check()
        sleep(2)
        print(po.success_text())
        assert po.success_text()=="信息提交成功!"
        function.insert_img(self.driver,"success_des.png")
        po.close_alert_windows()


if __name__ == "__main__":
    unittest.main()