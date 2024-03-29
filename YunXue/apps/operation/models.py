# operation/models.py

from datetime import datetime

from django.db import models

from course.models import Course
from users.models import UserProfile


class UserAsk(models.Model):
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('手机',max_length=11)
    course_name = models.CharField('课程名',max_length=50)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户咨询"


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField('评论',max_length=200)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "课程评论"


class UserFavorite(models.Model):
    FAV_TYPE = (
        (1,'公开课程'),
        (2,'高校机构'),
        (3,'授课讲师')
    )

    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField('数据id',default=0)
    fav_type = models.IntegerField(verbose_name='收藏类型',choices=FAV_TYPE,default=1)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户收藏"


class UserMessage(models.Model):
    user = models.IntegerField('接受用户id',default=0)
    message = models.CharField('消息内容',max_length=500, null=True)
    add_time = models.DateTimeField('添加时间', default=datetime.now)


    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户消息"


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "用户课程"



