#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: core.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-05 22:34:52 (CST)
# Last Update:星期日 2017-8-6 11:40:4 (CST)
#          By:
# Description:
# **************************************************************************
from flask import jsonify


class HTTPResponse(object):
    NORMAL_STATUS = '200'

    FORBIDDEN = '403'

    OTHER_ERROR = '500'

    STATUS_DESCRIPTION = {
        NORMAL_STATUS: 'normal',
        FORBIDDEN: 'You have no permission!',
        OTHER_ERROR: 'Other error'
    }

    def __init__(self,
                 status='200',
                 message='',
                 data=None,
                 description='',
                 pageinfo=None):
        self.status = status
        self.message = message or self.STATUS_DESCRIPTION.get(status)
        self.data = data
        self.description = description
        self.pageinfo = pageinfo

    def to_dict(self):
        response = {
            'status': self.status,
            'message': self.message,
            'data': self.data,
            'description': self.description,
        }
        if self.pageinfo is not None:
            response.update(pageinfo=self.pageinfo.as_dict())
        return response

    def to_response(self):
        response = self.to_dict()
        return jsonify(response)
