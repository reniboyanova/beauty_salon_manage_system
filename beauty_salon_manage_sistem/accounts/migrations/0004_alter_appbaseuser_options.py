# Generated by Django 4.1.3 on 2022-12-07 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_appbaseuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appbaseuser',
            options={'default_permissions': (), 'verbose_name': 'User'},
        ),
    ]
