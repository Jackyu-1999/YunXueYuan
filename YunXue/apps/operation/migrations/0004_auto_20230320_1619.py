# Generated by Django 2.0.2 on 2023-03-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20230315_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '公开课程'), (2, '高校机构'), (3, '授课讲师')], default=1, verbose_name='收藏类型'),
        ),
    ]
