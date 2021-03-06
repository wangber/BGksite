# Generated by Django 2.0 on 2019-08-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qingganpin', '0003_auto_20190802_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lisening',
            options={'verbose_name': '每日一听歌曲录', 'verbose_name_plural': '每日一听歌曲录'},
        ),
        migrations.AlterModelOptions(
            name='qingganwen',
            options={'verbose_name': '情感频文章', 'verbose_name_plural': '情感频文章'},
        ),
        migrations.AlterField(
            model_name='lisening',
            name='content',
            field=models.FileField(upload_to='dayting/', verbose_name='上传你的歌曲吧'),
        ),
        migrations.AlterField(
            model_name='lisening',
            name='date',
            field=models.DateField(verbose_name='发布日期'),
        ),
        migrations.AlterField(
            model_name='lisening',
            name='story',
            field=models.TextField(max_length=2000, verbose_name='写下你想分享的故事'),
        ),
        migrations.AlterField(
            model_name='lisening',
            name='topic',
            field=models.CharField(max_length=30, verbose_name='发布主题'),
        ),
        migrations.AlterField(
            model_name='qingganwen',
            name='content',
            field=models.FileField(upload_to='qingganwen/', verbose_name='文章上传'),
        ),
        migrations.AlterField(
            model_name='qingganwen',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='最近更新日期'),
        ),
        migrations.AlterField(
            model_name='qingganwen',
            name='topic',
            field=models.CharField(max_length=30, verbose_name='主题'),
        ),
    ]
