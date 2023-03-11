# course/urls.py

from django.urls import path,re_path
from .views import CourseListView, CourseDetailView

# 要写上app的名字
app_name = "course"

urlpatterns = [
    path('list/',CourseListView.as_view(),name='course_list'),
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
]