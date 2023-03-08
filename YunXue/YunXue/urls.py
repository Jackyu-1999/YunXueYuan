# MxOnline/urls.py

import xadmin

from django.urls import path
from users.views import LoginView
from django.views.generic import TemplateView
from users import views


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
]