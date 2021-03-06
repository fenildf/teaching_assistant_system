# Generated by Django 2.0.5 on 2018-06-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCollectIssue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='标题')),
                ('deadline', models.DateField(blank=True, null=True, verbose_name='截止时间')),
                ('content', models.TextField(default='', max_length=500, verbose_name='发布内容')),
                ('Issue_file', models.FileField(default='', upload_to='Issue_file/%Y/%m')),
            ],
        ),
    ]
