# Generated by Django 2.0.2 on 2023-03-14 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_is_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
            },
            bases=('course.course',),
        ),
    ]
