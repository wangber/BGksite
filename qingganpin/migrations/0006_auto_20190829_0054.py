# Generated by Django 2.0 on 2019-08-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qingganpin', '0005_auto_20190829_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qingganwen',
            name='content',
            field=models.TextField(max_length=3000, verbose_name='文章内容（建议使用MarkDown语法书写）'),
        ),
    ]
