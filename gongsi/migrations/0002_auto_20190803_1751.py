# Generated by Django 2.0 on 2019-08-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gongsi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gudong',
            options={'verbose_name': '股东', 'verbose_name_plural': '股东'},
        ),
        migrations.AlterModelOptions(
            name='zhizhu',
            options={'verbose_name': '宠物', 'verbose_name_plural': '宠物'},
        ),
        migrations.AlterField(
            model_name='gudong',
            name='latestday',
            field=models.DateField(auto_now=True, verbose_name='最近一次信息更新日期'),
        ),
        migrations.AlterField(
            model_name='zhizhu',
            name='zhuimage',
            field=models.FileField(upload_to='zhizhuimage/', verbose_name='上传一张最能代表它的图片吧'),
        ),
    ]