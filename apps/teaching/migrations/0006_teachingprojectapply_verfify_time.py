# Generated by Django 2.0.5 on 2018-06-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0005_auto_20180616_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachingprojectapply',
            name='verfify_time',
            field=models.DateField(blank=True, null=True, verbose_name='审核时间'),
        ),
    ]