# Generated by Django 2.0 on 2017-12-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='create_date',
            field=models.CharField(default='2017-12-03 19:27:21', max_length=40, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]