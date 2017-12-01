#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/28 17:31
"""
from mayi.test_case.page_obj import mayi_QR_page,login_page,landlord_nav_page,tenant_nav_page
from mayi.models import jiexi_QR,myunit
from selenium import webdriver
from time import sleep
import unittest

class TestQR(myunit.MyTest):
    '''二维码解析'''

    def login_online(self):
        '''线上登录'''
        login_page.LoginPage(self.driver).loginshow()
        login_page.LoginPage(self.driver).changeloginbyup()
        login_page.LoginPage(self.driver).username("18701016443")
        login_page.LoginPage(self.driver).password("18701016443")
        login_page.LoginPage(self.driver).imagecode1()
        login_page.LoginPage(self.driver).loginbyupdo()

    def public_google_downpage(self,url,p):
        # 进入谷歌下载页面
        self.driver.get("chrome://downloads/")
        sleep(2)

        # 打印body的所有内容，然后去截断获取自己想要的
        text = mayi_QR_page.MaYiQRPage(self.driver).text()

        sleep(2)
        text = text.split("\n")
        APP_name = text[5]
        APP_url = text[6]

        size = text[7].split("，")

        APP_size = size[1]
        sleep(2)
        print("")
        print("二维码所在位置：" + p)
        print("二维码解析结果：" + url)
        print("APP包名：" + APP_name)
        print("APP下载地址：" + APP_url)
        print("APP大小：" + APP_size)


    def test_nav_QR(self):
        '''11首页导航——APP首单立减5元——二维码'''
        p = "首页导航——APP首单立减5元——二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)


        #获取最新的二维码url，并传到解析方法中。也可直接把url直接传，考虑二维码url可能会改变，因此每次都获取最新的。
        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/v201510/images/commom/app.jpg")
        sleep(3)
        #打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        #下载按钮
        po.down_btn()
        sleep(2)

        #调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_bottom_QR(self):
        '''④首页底部二维码'''
        p = "首页底部二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        # 获取最新的二维码url，并传到解析方法中。也可直接把url直接传，考虑二维码url可能会改变，因此每次都获取最新的。
        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/v201510/images/commom/app.jpg")
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)


    def test_Androiddown_btn(self):
        '''③首页底部Android下载按钮'''
        p = "首页底部Android下载按钮"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com")
        po.js("var j = document.body.scrollTop = 4935")

        sleep(3)

        po.Androiddown_btn()
        url = "直接下载apk"
        sleep(3)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)


    def test_bottom_left_QR(self):
        '''⑥下载蚂蚁短租客户端手机注册立送5元——二维码'''
        p = "下载蚂蚁短租客户端手机注册立送5元——二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/v201510/images/commom/app.jpg")
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_bottom_left_Andriodbtn(self):
        '''⑤下载蚂蚁短租客户端手机注册立送5元——Android下载按钮'''
        p = "下载蚂蚁短租客户端手机注册立送5元——Android下载按钮"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com")
        sleep(3)
        po.js("var j = document.body.scrollTop = 1000")
        po.bottom_left_andriodbtn()
        url = "直接下载APK"
        sleep(3)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_APP50_QR(self):
        '''①APP50下载页面的二维码'''
        p = "APP50下载页面的二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/topic/app50/images/ewm.png")
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_APP50_andriodbtn(self):
        '''②APP50下载页面的Android下载按钮'''
        p = "APP50下载页面的Android下载按钮"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com/activity/app50")
        sleep(3)
        po.APP50_andriodbtn()
        url = "直接下载APK"
        sleep(3)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_order_banner_QR(self):
        '''12房东我的订单banner图第一张——二维码'''
        p = "房东我的订单banner图第一张——二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com")
        #登录
        self.login_online()
        sleep(5)
        landlord_nav_page.LandlordNavPage(self.driver).Iamlandlord()
        sleep(3)
        landlord_nav_page.LandlordNavPage(self.driver).close_weiChat()


        url = jiexi_QR.decode_qr(po.order_banner_QR())
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_index_rigit_QR(self):
        '''⑦首页右侧保洁合作下面——APP首单立减5元——二维码'''
        p = "首页右侧保洁合作下面——APP首单立减5元——二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com")
        po.js("var j = document.body.scrollTop = 1000")


        url = jiexi_QR.decode_qr(po.right_QR())
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_order_call_QR(self):
        '''13下单页——拨打电话——二维码'''
        p = "下单页——拨打电话——二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        po.opentest("http://www.mayi.com/room/851272901")


        url = jiexi_QR.decode_qr(po.call_QR())
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_tenant_order_QR(self):
        '''14房客我的订单右侧二维码'''
        p = "房客我的订单右侧二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)
        # po.opentest("http://www.mayi.com/")
        # self.login_online()
        # sleep(3)
        tenant_nav_page.TenantNavPage(self.driver).Iamtenant()


        url = jiexi_QR.decode_qr(po.tenant_order_QR())
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_msg_QR(self):
        '''⑩IM聊天的二维码'''
        p = "IM聊天的二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/v201510/images/app_down_im.png")
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # # 下载按钮
        # po.down_btn()
        # sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_landlord_zhaomu_QR(self):
        '''⑨PC房东招募的二维码'''
        p = "PC房东招募的二维码"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = jiexi_QR.decode_qr("http://staticnew.mayi.com/resourcesWeb/landlordRecruit/images/code.png")
        sleep(3)
        # 打开解析后的下载地址
        po.opentest(url)
        sleep(2)

        # # 下载按钮
        po.down_btn()
        sleep(2)

        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)


    def test_wap_downapp(self):
        '''wap底部弹层立即下载'''
        p = "wap页面底部弹层立即下载"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = "http://m.mayi.com/"
        po.opentest(url)
        sleep(2)
        po.wap_down_btn()
        sleep(2)
        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_wap_bottomdown(self):
        '''15wap页底部下载app'''
        p = "wap页底部下载app"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = "http://m.mayi.com/"
        po.opentest(url)
        sleep(2)
        po.js("var j = document.body.scrollTop=5536")
        po.wap_bottom_down()
        sleep(2)
        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_wap_lianxifangdong(self):
        '''房源详情页联系房东下载app'''
        p = "WAP房源详情页联系房东下载app"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = "http://m.mayi.com/room/851083925"

        po.opentest(url)
        sleep(2)
        po.lianxifangdong_down()
        sleep(2)
        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)

    def test_landlord_index(self):
        '''⑧房东主页下载app'''
        p = "房东主页下载app"
        po = mayi_QR_page.MaYiQRPage(self.driver)

        url = "http://m.mayi.com/landlord/landlordIndex/854597541/?client=false&roomId=851013710"

        po.opentest(url)
        sleep(2)
        po.landlord_index_down()
        sleep(2)
        # 调用公共函数，打印想获取的数据
        self.public_google_downpage(url,p)


if __name__ == "__main__":
    unittest.main()

