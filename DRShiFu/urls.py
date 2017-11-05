#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""DRShiFu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from ShiFu.Api.WebCenter import *
from ShiFu.Api.DRApi import *
from ShiFu.Api.DRManageApi import *
from ShiFu.Api.DRPublicApi import *

from ShiFu.views import *
from ShiFu.Api.WX.DRWeiXin import *

urlpatterns = [
    # API接口
    url(r'^admin/', admin.site.urls),
    url(r'^$', WebCenter.goHome),
    url(r'^user_main.html', WebCenter.goUserHome),
    url(r'^user_qx_orders.html', WebCenter.goUserQXOrder),

    url(r'^user_setup_orders.html', WebCenter.goSetupOrder),
    url(r'^user_wx_orders.html', WebCenter.goWXOrder),
    url(r'^user_remarks.html', WebCenter.goRemarks),
    url(r'^user_tickets.html', WebCenter.goUseTickes),
    url(r'^user_addresss.html', WebCenter.goAddress),
    url(r'^login_org.html', WebCenter.loginOrg),
    url(r'^login_emplyee.html', WebCenter.loginEmplyee),
    url(r'^user_add_address.html', WebCenter.addUserAddress),
    url(r'^suggest.html', WebCenter.goSuggest),
    url(r'^service_flow.html', WebCenter.goServiceFlow),
    url(r'^want_service.html', WebCenter.goServiceFlow),
    url(r'^index.html', WebCenter.goTest),
    url(r'^add_emplyee.html', WebCenter.goAddEmplyee),
    url(r'^order_detail_info.html', WebCenter.openOrderDetail),

    url(r'^begin_order.html', WebCenter.startOrder),


    url(r'^org_main.html', WebCenter.goOrgHome),
    url(r'^emplyee_main.html', WebCenter.goEmplyeeHome),

    url(r'^start_order_aj.html', WebCenter.goOrderAj),
    url(r'^start_order_gd_qx.html', WebCenter.goOrderGdQx),
    url(r'^start_order_qx.html', WebCenter.goOrderQx),
    url(r'^start_order_wx.html', WebCenter.goOrderWx),

    url(r'^api/user/$',DRApi.CommandDispatch),
    url(r'^api/manage/$',DRManageApi.CommandDispatch),
    url(r'^api/pub/$',DRPublicApi.CommandDispatch),

    # # # 授权
    # url(r'^auth/$', AuthView.as_view(), name='wx_auth'),
    # # 获取用户信息
    # url(r'^testWX$', GetUserInfoView.as_view(), name='get_user_info'),
    # # # 微信接口配置信息验证
    # url(r'^$', WxSignature.as_view(), name='signature'),
    # # 测试
    # url(r'^testWX$', DRWeiXin.applyAuth),


] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)