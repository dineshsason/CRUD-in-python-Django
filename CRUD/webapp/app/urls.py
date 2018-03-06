# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url,include
from . import views

urlpatterns = [ url('^$',views.Index,name='Index'),
                url(r'^add/$',views.add, name = 'add'),
                url(r'^edit/([0-9]+)/$',views.edit, name = 'edit'),
                url(r'^dele/([0-9]+)/$',views.dele, name = 'dele')
                ]

