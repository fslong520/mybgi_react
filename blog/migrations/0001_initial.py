# Generated by Django 2.1.2 on 2018-10-23 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='无主题', max_length=255, verbose_name='标题')),
                ('pubTime', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('changeTime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.CharField(default='佚名', max_length=255, verbose_name='作者')),
                ('content', models.TextField(default='', verbose_name='内容')),
            ],
            options={
                'ordering': ['pubTime'],
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='杂', max_length=255, verbose_name='栏目')),
            ],
            options={
                'verbose_name': '栏目',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', verbose_name='评论')),
                ('pubTime', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('changeTime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('floor', models.IntegerField(default='0', verbose_name='楼层')),
                ('article', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
            options={
                'ordering': ['pubTime'],
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='匿名', max_length=255, verbose_name='姓名')),
                ('email', models.EmailField(default='test@example.cpm', max_length=255, verbose_name='Email')),
                ('password', models.CharField(default='admin', max_length=255, verbose_name='密码')),
                ('profilePhoto', models.TextField(default='//tva1.sinaimg.cn/crop.318.608.1137.1137.180/3c1b9c69jw8f1ptze8k4hj21kw1ekakh.jpg', verbose_name='头像')),
                ('isAdmin', models.BooleanField(default=False, verbose_name='管理员权限')),
                ('regTime', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '小伙伴',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.Column'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.User'),
        ),
    ]
