#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/23 9:06
"""

from .base import Pyse
from mayi.models import mydef

class LandlordMicroshopManagerPage(Pyse):
    '''房东微店'''

    #保存二维码图片
    def save_img_btn(self):
        self.click("class=>save_img_btn")

    #查看我的微店
    def check_shop_btn(self):
        self.click("class=>check_shop_btn")

    #编辑微店
    def edit_weidian_btn(self):
        self.click("class=>edit_weidian_btn")

    #查看微店说明
    def view_again_btn(self):
        self.click("class=>view_again_btn")


    #编辑微店弹窗——微店名称
    def title(self):
        text = mydef.rad_word(5)
        self.clear("xpath=>/html/body/div[14]/div[5]/div/div[7]/div[2]/div[2]/input")
        self.type("xpath=>/html/body/div[14]/div[5]/div/div[7]/div[2]/div[2]/input",text)

    #编辑微店弹窗——微店介绍
    def shop_introduction(self):
        text = mydef.rad_word(10)
        self.clear("xpath=>/html/body/div[14]/div[5]/div/div[7]/div[2]/div[3]/textarea")
        self.type("xpath=>/html/body/div[14]/div[5]/div/div[7]/div[2]/div[3]/textarea",text)

    #编辑微店弹窗——保存
    def save_edit_btn(self):
        self.click("class=>save-edit-btn")


    #微店说明的文案
    def microshop_text(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[5]/div/div")
        return text



