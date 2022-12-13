# Generated by Django 4.1.3 on 2022-12-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingcustomerprocedure',
            options={'ordering': ['-select_date']},
        ),
        migrations.RemoveField(
            model_name='bookingcustomerprocedure',
            name='pick_a_date',
        ),
        migrations.AddField(
            model_name='bookingcustomerprocedure',
            name='select_date',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingcustomerprocedure',
            name='select_time',
            field=models.CharField(default='8:00', max_length=30),
        ),
    ]
