# -*- coding:utf-8 -*-
# __author__ = "shitou6"

from . import admin
@admin.route('/')
def index():
    return "this is admin!"