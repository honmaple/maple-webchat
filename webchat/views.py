#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: views.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-05 22:30:08 (CST)
# Last Update:星期日 2017-8-6 10:28:2 (CST)
#          By:
# Description:
# **************************************************************************
from flask import request, make_response, current_app
from flask.views import MethodView
from webchat.core import HTTPResponse
from webchat.msg import Msg
from webchat.action import TextAction, ImageAction
from hashlib import sha1


def check_signature(signature, timestamp, nonce):
    token = current_app.config['WEBCHAT_TOKEN']
    _list = [timestamp, nonce, token]
    _list.sort()
    s = ''.join(_list)
    if sha1(s.encode('utf-8')).hexdigest() == signature:
        return True
    return False


class HandleView(MethodView):
    def get(self):
        '''
        响应微信参数
        '''
        query_dict = request.args.to_dict()
        signature = query_dict.pop('signature', '')
        timestamp = query_dict.pop('timestamp', '')
        nonce = query_dict.pop('nonce', '')
        echostr = query_dict.pop('echostr', '')
        if check_signature(signature, timestamp, nonce):
            return make_response(echostr)
        return HTTPResponse(HTTPResponse.FORBIDDEN).to_response()

    def post(self):
        query_dict = request.args.to_dict()
        signature = query_dict.pop('signature', '')
        timestamp = query_dict.pop('timestamp', '')
        nonce = query_dict.pop('nonce', '')
        if check_signature(signature, timestamp, nonce):
            rec = request.stream.read()
            if len(rec) == 0:
                return make_response('success')
            msg = Msg(rec)
            if msg.is_text:
                return self.render_text(msg)
            elif msg.is_image:
                return self.render_image(msg)
        return make_response('success')

    def render_image(self, msg):
        parse = msg.parse_image()
        media_id = parse.pop('MediaId', '')
        response = msg.send_image(ImageAction(media_id).send())
        return make_response(response)

    def render_text(self, msg):
        parse = msg.parse_text()
        content = parse.pop('Content', '')
        response = msg.send_text(TextAction(content).send())
        return make_response(response)
