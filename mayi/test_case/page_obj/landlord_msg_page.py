#!/usr/bin/env python
# encoding: utf-8

"""
@version: python.3.6
@author: zhangjiaheng
@software: PyCharm
@time: 2017/9/22 16:29
"""
from .base import Pyse
from models import mydef

class LandlordMsgPage(Pyse):
    '''消息通知'''

    #回复
    def return_msg(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div/div[1]/div[2]/ul/li[2]/span/span/a")

    #查看
    def look(self):
        self.click("xpath=>html/body/div[14]/div[5]/div/div/div/div[1]/div[2]/ul/li[1]/a")

    #IM输入区域
    def IM_text(self):
        text = mydef.rad_word(5)
        self.type("xpath=>html/body/div[10]/div[2]/div[6]/div[1]/textarea",text)

    #IM发送按钮
    def send_msg(self):
        self.click("xpath=>html/body/div[10]/div[2]/div[6]/div[1]/div[3]/button")

    #缩小按钮
    def shrink(self):
        self.click("xpath=>html/body/div[10]/span")

    #聊天记录
    def msg_record(self):
        text = self.get_text("xpath=>html/body/div[14]/div[5]/div/div[2]")
        return text

