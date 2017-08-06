#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: menu.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-06 10:51:38 (CST)
# Last Update:星期日 2017-8-6 11:39:42 (CST)
#          By:
# Description:
# **************************************************************************
from flask import current_app
import requests


class Basic(object):
    def __init__(self):
        app_id = current_app.config['WEBCHAT_APPID']
        app_secret = current_app.config['WEBCHAT_APPSECRET']
        self.token_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
                          "client_credential&appid=%s&secret=%s" %
                          (app_id, app_secret))
        self.left_time = 0
        self.access_token = ''

    def _get_access_token(self):
        response = requests.get(self.token_url)
        rsp = response.json()
        return rsp['access_token']

    def get_access_token(self):
        if self.left_time < 10:
            return self._get_access_token()
        return self.access_token


class Menu(object):
    def __init__(self, acceess_token):
        self.acceess_token = acceess_token

    def create(self, data):
        url = ("https://api.weixin.qq.com/cgi-bin/menu"
               "/create?access_token=%s") % self.acceess_token
        response = requests.post(url, data=data)
        return response.text

    def query(self):
        url = ("https://api.weixin.qq.com/cgi-bin/menu"
               "/get?access_token=%s") % self.acceess_token
        response = requests.get(url)
        return response.text

    def delete(self):
        url = ("https://api.weixin.qq.com/cgi-bin/menu"
               "/delete?access_token=%s") % self.acceess_token
        response = requests.get(url)
        return response.text

    def get_current_selfmenu_info(self):
        url = (
            "https://api.weixin.qq.com/cgi-bin/"
            "get_current_selfmenu_info?access_token=%s") % self.acceess_token
        response = requests.get(url)
        return response.text


WEBCHAT_MENU = {
    "button": [
        {
            "type": "click",
            "name": "你好,世界",
            "key": "hi"
        }, {
            "name": "自由",
            "sub_button": [
                {
                    "type": "click",
                    "name": "爱情诚可贵",
                    "key": "love",
                    "sub_button": []
                }, {
                    "type": "click",
                    "name": "自由价更高",
                    "key": "freedom",
                    "sub_button": []
                }
            ]
        }
    ]
}

if __name__ == '__main__':
    access_token = Basic().get_access_token()
    menu = Menu(access_token)
    a = menu.create(WEBCHAT_MENU)
    print(a)
