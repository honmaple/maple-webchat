#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: runserver.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-05-08 18:25:14 (CST)
# Last Update:星期日 2017-8-6 11:40:17 (CST)
#          By:
# Description:
# **************************************************************************
from webchat import create_app
from werkzeug.contrib.fixers import ProxyFix

app = create_app('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(port=8000)
