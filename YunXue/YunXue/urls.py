# MxOnline/urls.py

import xadmin

from django.urls import path,include,re_path
from users.views import ForgetPwdView, ModifyPwdView, ResetView,LogoutView
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView,ActiveUserView
from organization.views import OrgView
from django.views.static import serve
from YunXue.settings import MEDIA_ROOT

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
    path("org/", include('organization.urls', namespace="org")),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT })

]