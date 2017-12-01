#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/28 17:04
"""
from .base import Pyse

class MaYiQRPage(Pyse):
    '''PC网页二维码'''
    # url = "/"


    #首页导航——APP首单立减5元——二维码
    def nav_qr(self):
        self.move_to_element("xpath=>/html/body/div[1]/div/ul/li[3]/div/a")
        QR_url = self.get_attribute("xpath=>/html/body/div[1]/div/ul/li[3]/div/div/img","src")
        return QR_url

    #首页右侧保洁合作——APP首单立减5元——二维码
    def right_QR(self):
        self.move_to_element("xpath=>//*[@id='app-click']/a/b")
        QR_url = self.get_attribute("xpath=>//*[@id='top_div']/img","src")
        return QR_url


    #谷歌下载页面文案打印
    def text(self):
        text = self.get_text("xpath=>/html/body")
        return text

    #首页底部二维码
    def bottom_QR(self):
        QR_url = self.get_attribute("css=>.mt10,.app_download_qr","src")
        return QR_url

    #首页底部Android下载
    def Androiddown_btn(self):
        self.click("css=>.app,.mt10 t-center")

    #下载蚂蚁短租客户端手机注册立送5元——二维码
    def bottom_left_QR(self):
        QR_url = self.get_attribute("xpath=>//*[@id='floatingLayer']/div[1]/div[2]/div[1]/img","src")
        return QR_url

    #下载蚂蚁短租客户端手机注册立送5元——下载按钮
    def bottom_left_andriodbtn(self):
        self.click("xpath=>//*[@id='floatingLayer']/div[1]/div[2]/div[2]/a[2]")

    #APP50下载页面的Android下载按钮
    def APP50_andriodbtn(self):
        self.click("xpath=>//*[@id='Android']/img")

    #房东banner图上的二维码
    def order_banner_QR(self):
        QR_url = self.get_attribute("xpath=>//*[@id='box']/div[1]/ul/li[1]/img","src")
        return QR_url

    #下载页——拨打电话——二维码
    def call_QR(self):
        self.move_to_element("class=>call-phone")
        QR_url = self.get_attribute("class=>chat_ma","src")
        return QR_url

    #房客订单管理右侧
    def tenant_order_QR(self):
        QR_url = self.get_attribute("xpath=>//*[@id='wx']/a/img","src")
        return QR_url

    #房东招募
    def landlord_zhaomu_QR(self):
        QR_url = self.get_attribute("xpath=>/html/body/div[14]/div[2]/div[2]/div[2]/div[3]/div[3]/img","src")
        return QR_url
    # def close_(self):
    #     self.click("xpath=>//*[@id='floatingLayer']/div[1]/div[2]/div[5]/img")

    # 下载页——下载按钮
    def down_btn(self):
        self.click("xpath=>/html/body/section/div[1]/div/a")


    #WAP页下载app
    def wap_down_btn(self):
        self.click("id=>app_download")

    #WAP页底部下载
    def wap_bottom_down(self):
        self.click("class=>appdownload")

    #联系房东
    def lianxifangdong_down(self):
        self.click("class=>pBox")

    #房东主页下载app
    def landlord_index_down(self):
        self.click("xpath=>//*[@id='indexPage']/div[1]/div[3]/p[3]/a")