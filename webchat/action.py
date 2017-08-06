#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: action.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-06 09:55:57 (CST)
# Last Update:星期日 2017-8-6 10:25:38 (CST)
#          By:
# Description:
# **************************************************************************


class Action(object):
    def __init__(self, content):
        self.content = content

    def send(self):
        pass


class TextAction(Action):
    def send(self):
        text = self.content.lower()
        if text == 'joke':
            return '哈哈哈'
        return '欢迎关注红枫林!'


class ImageAction(Action):
    def send(self):
        text = str(self.content, encoding="utf-8")
        return text
