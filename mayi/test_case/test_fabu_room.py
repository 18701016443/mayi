#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 11:10
"""
from mayi.test_case.page_obj import fabu_room_page,login_page
from mayi.models import myunit,function
import unittest
from time import sleep

class TestFabuRoom(myunit.MyTest):
    '''发布房源'''
    def test_fabu_room(self):
        login_page.LoginPage(self.driver).login()
        po = fabu_room_page.FabuRoomPage(self.driver)
        po.fabu_room()
        sleep(2)
        po.close_window()
        sleep(2)
        po.room_type()
        sleep(2)
        po.dixiashi()
        sleep(2)
        po.room_size()
        po.roomnum()
        sleep(2)
        po.privatetoiletnum()
        po.guestnum()
        sleep(2)
        po.big_bed()
        po.middle_bed()
        po.single_bed()
        sleep(2)
        po.free_facilities()
        po.stock()
        sleep(2)
        po.baseSave()
        sleep(2)


        po.title()
        sleep(2)
        po.intro()
        sleep(2)
        po.detailSave()


        po.up_picture()
        sleep(2)
        po.nextstep()

        po.dayprice()
        po.addbed()
        po.refunddays()
        sleep(2)
        po.four_save()

        po.cert_type1()
        po.SWFUpload_4()
        po.SWFUpload_6()
        po.other()
        po.five_save()
        sleep(2)
        po.alert_windows()
        print(po.submit_success())

        assert po.submit_success() == "房间信息已提交！"

        function.insert_img(self.driver,"fabu_success.png")


if __name__ == "__main__":
    unittest.main()