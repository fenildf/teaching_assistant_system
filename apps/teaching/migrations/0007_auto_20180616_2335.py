# Generated by Django 2.0.5 on 2018-06-16 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0006_teachingprojectapply_verfify_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachingprojectapply',
            old_name='verfify_time',
            new_name='verify_time',
        ),
    ]
