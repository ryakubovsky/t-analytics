# Generated by Django 2.2.6 on 2019-12-02 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0002_auto_20191202_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vkauth',
            name='vkUserId',
            field=models.IntegerField(),
        ),
    ]