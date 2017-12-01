#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 10:34
"""
from .base import Pyse
from mayi.models import mydef

class LandlordOnlineEditdata(Pyse):
    '''已上线——修改资料'''
    # url = "/"

    #修改资料
    def editdata(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div[1]/div[1]/div[2]/div[5]/ul/li[3]/a")

    #判断“修改资料审核中  【关闭】”是否存在,若存在则点击关闭
    def div_is_13or15(self):
        self.is_element_exist("xpath=>html/body/div[14]/div[2]/div/div/div[1]/form/div[1]/p/em")


    #房源描述
    def fy_des(self):
        self.click("id=>fy_des")

    #房源图片
    def fy_picture(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/ul/li[3]")

    #价格要求
    def fy_price(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/ul/li[4]")

    #修改房源弹窗文案
    def editsuccess_text(self):
        text = self.get_text("xpath=>html/body/div[16]/div/div/div/div[2]/div[1]")
        return text

    #修改房源弹窗——我知道了
    def auditLodgeConfirmBtn(self):
        self.click("id=>auditLodgeConfirmBtn")


    #房屋类型
    # def room_type(self,div):
    #     self.click("xpath=>html/body/div["+div+"]/div[2]/div/div/div[1]/form/div[2]/dl[2]/dd/select/option["+mydef.rad_num(1,18)+"]")

    #是否地下室
    def dixiashi(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[1]/form/div[1]/dl[3]/dd/select/option[" + mydef.rad_num(1,4) + "]")

    #被单更换
    def sheet_replacement(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[1]/form/div[1]/dl[9]/dd/select/option["+mydef.rad_num(1,3)+"]")

    #保存
    def save(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[1]/form/div[2]/a")

############房源描述

    #地理位置编辑
    # def EditAddress(self):
    #     self.click("id=>EditAddress")

    # #弹窗确认
    # def changePosition(self):
    #     self.click("id=>changePosition")


    #房源描述保存
    def fydes_save(self):
        self.click("xpath=>//*[@id='describeform']/div[2]/a")


###########房源图片

    #上传图片
    def SWFUpload_0(self):
        self.click("id=>SWFUpload_0")

    #设为封面
    def setcover(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[3]/div[2]/form/div[2]/div[1]/ul/li[2]/div/a[1]")

    #删除图片
    def del_pic(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[3]/div[2]/form/div[2]/div[1]/ul/li[1]/div/a[2]")

    #保存
    def pic_save(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[3]/div[2]/form/div[2]/div[2]/a")

############价格要求

    #价格要求
    def price(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/ul/li[4]")

    #特殊价是否打折——是
    def specialdiscount_yes(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[2]/ul/li[4]/div/input[1]")

    # 特殊价是否打折——否
    def specialdiscount_no(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[2]/ul/li[4]/div/input[2]")

    #入住时间
    def checkintimeStr(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[1]/div/select/option["+mydef.rad_num(1,24)+"]")

    #退房时间
    def checkouttimeStr(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[2]/div/select/option["+mydef.rad_num(1,24)+"]")

    #接待外宾
    def foreigner_yes(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[6]/div/label[1]/input")

    def foreigner_no(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[6]/div/label[2]/input")

    #发票
    def bill_yes(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[7]/div/label[1]/input")
    def bill_no(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[3]/ul/li[7]/div/label[2]/input")

    #保存
    def price_save(self):
        self.click("xpath=>html/body/div[14]/div[2]/div/div/div[4]/form/div[4]/a")
