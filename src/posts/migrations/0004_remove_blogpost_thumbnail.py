# Generated by Django 3.1.7 on 2023-05-13 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230513_0053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
    ]