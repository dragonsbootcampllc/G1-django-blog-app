# Generated by Django 4.2.1 on 2023-10-09 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_comment_parent_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
    ]