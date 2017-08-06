#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: msg.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-05 23:38:19 (CST)
# Last Update:星期日 2017-8-6 10:14:20 (CST)
#          By:
# Description:
# **************************************************************************
import xml.etree.ElementTree as ET
from time import time


class Msg(object):
    def __init__(self, web_data):
        self.xml_data = ET.fromstring(web_data)
        self.msg_type = self.xml_data.find('MsgType').text

    def _parse(self):
        return {
            'ToUserName': self.xml_data.find('ToUserName').text,
            'FromUserName': self.xml_data.find('FromUserName').text,
            'CreateTime': self.xml_data.find('CreateTime').text,
            'MsgType': self.xml_data.find('MsgType').text,
            'MsgId': self.xml_data.find('MsgId').text
        }

    def parse(self):
        if self.is_text:
            return self.parse_text()
        elif self.is_image:
            return self.parse_image()

    def parse_text(self):
        _dict = self._parse()
        _dict.update(
            Content=self.xml_data.find('Content').text.encode("utf-8"))
        return _dict

    def parse_image(self):
        _dict = self._parse()
        _dict.update(
            PicUrl=self.xml_data.find('PicUrl').text.encode("utf-8"),
            MediaId=self.xml_data.find('MediaId').text.encode("utf-8"))
        return _dict

    def send(self, content=''):
        if not content:
            return 'success'
        if self.is_text:
            return self.send_text(content)
        elif self.is_image:
            return self.send_image(content)
        return 'success'

    def send_text(self, content):
        _dict = {
            'ToUserName': self.xml_data.find('FromUserName').text,
            'FromUserName': self.xml_data.find('ToUserName').text,
            'CreateTime': int(time())
        }
        _dict.update(Content=content)
        xmlform = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return xmlform.format(**_dict)

    def send_image(self, media_id):
        _dict = {
            'ToUserName': self.xml_data.find('FromUserName').text,
            'FromUserName': self.xml_data.find('ToUserName').text,
            'CreateTime': int(time())
        }
        _dict.update(MediaId=media_id)
        xmlform = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[image]]></MsgType>
        <Image>
        <MediaId><![CDATA[{MediaId}]]></MediaId>
        </Image>
        </xml>
        """
        return xmlform.format(**_dict)

    @property
    def is_image(self):
        return self.msg_type == 'image'

    @property
    def is_text(self):
        return self.msg_type == 'text'
