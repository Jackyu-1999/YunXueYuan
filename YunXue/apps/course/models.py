# course/models.py

from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher


class Course(models.Model):
    DEGREE_CHOICES = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    name = models.CharField("课程名",max_length=50)
    desc = models.CharField("课程描述",max_length=300)
    detail = models.TextField("课程详情")
    degree = models.CharField('难度',choices=DEGREE_CHOICES, max_length=2)
    learn_times = models.IntegerField("学习时长(分钟数)",default=0)
    students = models.IntegerField("学习人数",default=0)
    fav_nums = models.IntegerField("收藏人数",default=0)
    image = models.ImageField("封面图",upload_to="courses/%Y/%m",max_length=100, blank=True)
    click_nums = models.IntegerField("点击数",default=0)
    tag = models.CharField('课程标签',default='',max_length=10)
    add_time = models.DateTimeField("添加时间",default=datetime.now,)
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构", null=True, blank=True)
    category = models.CharField("课程类别",max_length=20, default="")
    teacher = models.ForeignKey(Teacher,verbose_name='讲师',null=True,blank=True,on_delete=models.CASCADE)
    youneed_know = models.CharField('课程须知',max_length=300,default='')
    teacher_tell = models.CharField('你能学到',max_length=300,default='')
    is_banner = models.BooleanField('是否轮播',default=False)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_course_lesson(self):
        #获取课程的章节
        return self.lesson_set.all()

    def get_zj_nums(self):
        #获取课程的章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = '章节数'   #在后台显示的名称

    def get_learn_users(self):
        #获取这门课程的3个学习用户
        return self.usercourse_set.all()[:3]

    def get_comment(self):
        #获取评论
        return self.coursecomments_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    '''显示轮播课程'''
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        #这里必须设置proxy=True，这样就不会再生成一张表，同时还具有Model的功能
        proxy = True

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name='课程',on_delete=models.CASCADE)
    name = models.CharField("章节名",max_length=100)
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def get_lesson_vedio(self):
        #获取章节所有视频
        return self.video_set.all()

    def __str__(self):
        return self.name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="章节",on_delete=models.CASCADE)
    name = models.CharField("视频名",max_length=100)
    url = models.CharField('访问地址',default='',max_length=200)
    learn_times = models.IntegerField("学习时长(分钟数)",default=0)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField("名称",max_length=100)
    download = models.FileField("资源文件",upload_to="course/resource/%Y/%m",max_length=100)
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
