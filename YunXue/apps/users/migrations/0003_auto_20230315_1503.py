# Generated by Django 2.0.2 on 2023-03-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230313_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='image/default.png', upload_to='image/%Y%m'),
        ),
    ]
