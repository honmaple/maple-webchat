#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2017 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2017-08-05 22:29:48 (CST)
# Last Update:星期日 2017-8-6 0:21:17 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Flask
from webchat.views import HandleView
import os


def create_app(config):
    templates = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'templates'))
    static = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

    app = Flask(__name__, template_folder=templates, static_folder=static)
    app.config.from_object(config)
    app.add_url_rule('/handle', view_func=HandleView.as_view('handle'))
    return app
