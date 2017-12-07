#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/20 10:32
"""
from .base import Pyse
from models import mydef
import os
from time import sleep

class FabuRoomPage(Pyse):
    '''免费发布房源'''
    # url = "/"

# **********第一步定位开始**********

    #免费发布房源
    def fabu_room(self):
        self.click("link_text=>免费发布房源")

    #关闭蚂蚁短租房源合作标准框
    def close_window(self):
        self.click("class=>z_close")

    #房屋类型
    def room_type(self):
        self.click("xpath=>/html/body/div[14]/div[3]/form/div[1]/dl[2]/dl[2]/dd/select/option["+ mydef.rad_num(1,18)+"]")


    #是否地下室
    def dixiashi(self):
        self.click("xpath=>/html/body/div[14]/div[3]/form/div[1]/dl[2]/dl[3]/dd/select/option[" + mydef.rad_num(1,4) + "]")

    #房屋面积
    def room_size(self):
        size = mydef.rad_num(1, 999)
        self.type("id=>area",size)

    #户型
        #室
    def roomnum(self):
        self.click("xpath=>//*[@id='roomnum']/option["+ mydef.rad_num(1,11) +"]")
        #厅
    def parlor(self):
        self.click("xpath=>//*[@id='parlor']/option["+ mydef.rad_num(1,12) +"]")
        #厨
    def cookhouse(self):
        self.click("xpath=>//*[@id='cookhouse']/option["+mydef.rad_num(1,12)+"]")
        #阳台
    def balcony(self):
        self.click("xpath=>//*[@id='balcony']/option["+ mydef.rad_num(1,12) +"]")

    #卫生间
        #独立
    def privatetoiletnum(self):
        self.click("xpath=>//*[@id='privatetoiletnum']/option["+mydef.rad_num(2,12)+"]")
        #公共
    def publictoiletnum(self):
        self.click("xpath=>//*[@id='publictoiletnum']/option["+mydef.rad_num(1,12)+"]")

    #可住人数
    def guestnum(self):
        self.click("xpath=>//*[@id='guestnum']/option["+mydef.rad_num(2,11)+"]")

    #床数
        #双人床（大）
    def big_bed(self):
        self.click("xpath=>//*[@id='双人床（大，宽2m左右）']/option["+mydef.rad_num(1,12)+"]")
        #双人床（中）
    def middle_bed(self):
        self.click("xpath=>//*[@id='双人床（中，宽1.8m左右）']/option["+ mydef.rad_num(1,12)+"]")
        #双人床（小）
    def small_bed(self):
        self.click("xpath=>//*[@id='双人床（小，宽1.5m左右）']/option["+mydef.rad_num(1,12)+"]")
        #单人床
    def single_bed(self):
        self.click("xpath=>//*[@id='单人床']/option["+ mydef.rad_num(1,12)+"]")
        #双层床
    def bunk_bed(self):
        self.click("xpath=>//*[@id='双层床']/option["+mydef.rad_num(1,12)+"]")
        #单人沙发床
    def single_sofa_bed(self):
        self.click("xpath=>//*[@id='单人沙发床']/option["+mydef.rad_num(1,12)+"]")
        #双人沙发床
    def double_sofa_bed(self):
        self.click("xpath=>//*[@id='双人沙发床']/option["+mydef.rad_num(1,12)+"]")
        #儿童床
    def chile_bed(self):
        self.click("xpath=>//*[@id='儿童床']/option["+mydef.rad_num(1,12)+"]")
        #婴儿床
    def baby_bed(self):
        self.click("xpath=>//*[@id='婴儿床']/option["+mydef.rad_num(1,12)+"]")
        #榻榻米
    def tatami(self):
        self.click("xpath=>//*[@id='榻榻米']/option["+mydef.rad_num(1,12)+"]")
        #圆床
    def circle_bed(self):
        self.click("xpath=>//*[@id='圆床']/option["+mydef.rad_num(1,12)+"]")
        #气垫床
    def air_bed(self):
        self.click("xpath=>//*[@id='气垫床']/option["+mydef.rad_num(1,12)+"]")
        #炕床
    def kang_bed(self):
        self.click("xpath=>//*[@id='炕床']/option["+mydef.rad_num(1,12)+"]")

    #被单更换
    def sheet_replacement(self):
        self.click("xpath=>/html/body/div[14]/div[3]/form/div[1]/dl[2]/dl[9]/dd/select/option["+mydef.rad_num(1,3)+"]")

    #配套设施
        #免费项（循环勾选搜索项）
    def free_facilities(self):
        inputs = self.get_elements("name=>supporting")
        for i in inputs:
            if i.get_attribute("type") == "checkbox":
                i.click()

        #收费项（循环勾选所有项）
    def pri_facilities(self):
        inputs = self.get_elements("name=>chargeSupporting")
        for i in inputs:
            if i.get_attribute("type") == "checkbox":
                i.click()

    #提供服务（常见服务）
    def commonService(self):
        inputs = self.get_elements("name=>commonService")
        for i in inputs:
            if i.get_attribute("type")=="checkbox":
                i.click()

    #房源别名
    def alias(self):
        alias = mydef.rad_word(5)
        self.type("name=>alias",alias)

    #同类房源
    def stock(self):
        stock = mydef.rad_num(1,10)
        self.type("id=>stock",stock)

    #保存下一步
    def baseSave(self):
        self.click("id=>baseSave")


 # **********第二步定位开始**********

    #特色标题
    def title(self):
        title = "张佳恒测试"+mydef.rad_word(2)
        self.clear("id=>title")
        self.type("id=>title",title)

    #房屋内部情况介绍（50字以上）
    def intro(self):
        intro = mydef.rad_word(50)
        self.clear("id=>intro")
        self.type("id=>intro",intro)

    #地理位置/地标建筑
    def landmark(self):
        landmark = mydef.rad_word(10)
        self.clear("id=>landmark")
        self.type("id=>landmark",landmark)

    #交通状况
    def traffic(self):
        traffic = mydef.rad_word(10)
        self.clear("id=>traffic")
        self.type("id=>traffic",traffic)

    #周边生活设施
    def surroundings(self):
        surroundings = mydef.rad_word(10)
        self.clear("id=>surroundings")
        self.type("id=>surroundings",surroundings)

    #您有什么话想对房客说
    def userule(self):
        userule = mydef.rad_word(10)
        self.clear("id=>userule")
        self.type("id=>userule",userule)

    #其他
    def otherintro(self):
        otherintro = mydef.rad_word(10)
        self.clear("id=>otherintro")
        self.type("id=>otherintro",otherintro)
    #保存下一步
    def detailSave(self):
        self.click("id=>detailSave")

#**********第三步定位**********

    #上传图片
    def up_picture(self):
        for i in range(7):
            self.click("id=>SWFUpload_0")
            sleep(5)
            os.system("D:/python/mayi/data/up.exe")
            sleep(1)

    #保存下一步
    def nextstep(self):
        self.click("id=>nextstep")

#**********第四步定位**********

        #每日价格（60以上）
    def dayprice(self):
        dayprice = mydef.rad_num(60,9999)
        self.clear("id=>dayprice")
        self.type("id=>dayprice",dayprice)

    #周末特殊价
    def weekendtype(self):
        num = mydef.rad_num(1,5)
        self.click("xpath=>//*[@id='weekendtype']/option["+num+"]")
        if num !=1:
            weekendprice = mydef.rad_num(60,200)
            self.clear("id=>weekendprice")
            self.type("id=>weekendprice",weekendprice)

    #入住满7天
    def weekpriceRet(self):
        weekpriceRet = mydef.rad_num(5,10)
        self.clear("id=>weekpriceRet")
        self.type("id=>weekpriceRet",weekpriceRet)

    #入住满30天
    def monthpriceRet(self):
        monthpriceRet = mydef.rad_num(5,10)
        self.clear("id=>monthpriceRet")
        self.type("id=>monthpriceRet",monthpriceRet)

    #特殊价是否参与打折
    def specialdiscount_yes(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[1]/ul/li[4]/div/input[1]")

    def specialdiscount_no(self):
        self.click("name=>/html/body/div[14]/div[2]/form/div[1]/ul/li[4]/div/input[2]")

    #押金
    def deposit(self):
        deposit = mydef.rad_num(1,10)
        self.clear("id=>deposit")
        self.type("id=>deposit",deposit)

    #能否加床
    def addbed(self):
        num = mydef.rad_num(1,3)
        self.click("xpath=>//*[@id='addbed']/option["+num+"]")
        if num==1:
            num1= mydef.rad_num(1,3)
            self.click("xpath=>//*[@id='addbedyesorno']/option["+num1+"]")
            if num1 ==2:
                addbed_price = mydef.rad_num(1,100)
                self.type("id=>addbed_price",addbed_price)

    #能否加床说明
    def addbed_more(self):
        addbed_more = mydef.rad_word(5)
        self.clear("id=>addbed_more")
        self.type("id=>addbed_more",addbed_more)

    # 能否做饭
    def cook(self):
        num = mydef.rad_num(1,3)
        self.click("xpath=>//*[@id='cook']/option["+num+"]")
        if num ==1:
            num1 = mydef.rad_num(1,3)
            self.click("xpath=>//*[@id='cookyesorno']/option["+num1+"]")
            if num1 ==2:
                cook_price = mydef.rad_num(1,100)
                self.type("id=>cook_price",cook_price)
    #能否做饭说明
    def cook_more(self):
        cook_more=mydef.rad_word(5)
        self.type("id=>cook_more",cook_more)

    #清洁费
    def upto(self):
        num = mydef.rad_num(1,3)
        self.click("xpath=>//*[@id='upto']/option["+num+"]")
        if num ==1:
            upto_price = mydef.rad_num(1,100)
            self.type("id=>upto_price",upto_price)

    #清洁费说明
    def upto_more(self):
        upto_more = mydef.rad_word(5)
        self.type("id=>upto_more",upto_more)

    #电费说明
    def electric_more(self):
        electric_more = mydef.rad_word(5)
        self.type("id=>electric_more",electric_more)

    #其他费用说明
    def othercharge_more(self):
        othercharge_more = mydef.rad_word(5)
        self.type("id=>othercharge_more",othercharge_more)

    #退款规则：如房客想取消预订，您的退款规则是
    def refunddays(self):
        self.click("xpath=>//*[@id='refunddays']/option["+mydef.rad_num(2,4)+"]")

    #入住时间
    def checkintimeStr(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[1]/div/select/option["+mydef.rad_num(1,24)+"]")

    #退房时间
    def checkouttimeStr(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[2]/div/select/option["+mydef.rad_num(1,24)+"]")

    #接待时间
    def shopTimeStart(self):
        self.click("xpath=>//*[@id='shopTimeStart']/option["+mydef.rad_num(1,24)+"]")

    def shopTimeEnd(self):
        self.click("xpath=>//*[@id='shopTimeEnd']/option["+mydef.rad_num(1,24)+"]")

    #最少天数
    def mindays(self):
        self.click("xpath=>//*[@id='mindays']/option["+mydef.rad_num(1,11)+"]")

    #最多天数
    def maxdays(self):
        maxdays = mydef.rad_num(1,10)
        self.type("id=>maxdays",maxdays)

    #接待外宾
    def foreigner_yes(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[6]/div/label[1]/input")

    def foreigner_no(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[6]/div/label[2]/input")

    #发票
    def bill_yes(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[7]/div/label[1]/input")
    def bill_no(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[3]/ul/li[7]/div/label[2]/input")

    #保存下一步
    def four_save(self):
        self.click("xpath=>/html/body/div[14]/div[2]/form/div[4]/a")

#**********第五步定位**********

    #房屋是我自己的，我要上传房产证照片
    def cert_type1(self):
        self.click("id=>cert_type1")

    #房屋是租的，我要上传租房合同照片
    def cert_type2(self):
        self.click("id=>cert_type2")

    #房产证首页
    def SWFUpload_4(self):
        self.click("id=>SWFUpload_4")
        sleep(5)
        os.system("D:/python/mayi/data/up.exe")

    #房产证尾页
    def SWFUpload_6(self):
        self.click("id=>SWFUpload_6")
        sleep(5)
        os.system("D:/python/mayi/data/up.exe")

    def other(self):
        self.click("id=>SWFUpload_7")
        sleep(5)
        os.system("D:/python/mayi/data/up.exe")

    #保存下一步
    def five_save(self):
        self.click("xpath=>/html/body/div[14]/div[5]/div")

    #信息弹窗
    def alert_windows(self):
        self.click("xpath=>//*[@id='xubox_layer1']/div[1]/span/a")

    def submit_success(self):
        text = self.get_text("xpath=>/html/body/div[14]/div[2]/div/dl/dd/h3")
        return text