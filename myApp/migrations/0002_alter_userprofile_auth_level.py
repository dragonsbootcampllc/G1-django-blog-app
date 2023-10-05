# Generated by Django 4.2.1 on 2023-10-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='auth_level',
            field=models.CharField(choices=[('viewer', 'Viewer'), ('writer', 'Writer'), ('admin', 'Admin'), ('manager', 'Manager')], max_length=10, null=True),
        ),
    ]
