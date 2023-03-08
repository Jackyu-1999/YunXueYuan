# MxOnline/urls.py

import xadmin

from django.urls import path,include,re_path
from users.views import ForgetPwdView, ModifyPwdView, ResetView,LogoutView
from django.views.generic import TemplateView
from users.views import LoginView,RegisterView,ActiveUserView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('logout/',LogoutView.as_view(),name = 'logout'),
    path('register/',RegisterView.as_view(),name = 'register'),
    path('captcha/',include('captcha.urls')),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),

]