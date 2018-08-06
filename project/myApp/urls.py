# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhangcs
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # 路由至主页
    url(r'^$', views.Index),
    url(r'^index.html/$', views.Index1),
    url(r'^(\d+)/$', views.detail),
    # 路由至grades
    url(r'^grades/$', views.grades),
    # 路由至students
    url(r'^students/$', views.students),
    # 查看属性
    url(r'^attribles/$', views.attribles),
    # 使用get获取网址中的值
    url(r'^get1/$', views.get1),
    url(r'^get2/$', views.get2),
    # 使用post获取网址中的值
    # 显示注册界面
    url(r'^showregistered/$', views.showregistered),
    url(r'^showregistered/registered/$', views.registered),
    # 测试response属性
    url(r'^response/$', views.response),
    # 测试cookie
    url(r'^cookieTest/$', views.cookieTest),
    url(r'^redirect1/$', views.redirect1),
    url(r'^redirect2/$', views.redirect2),
]
