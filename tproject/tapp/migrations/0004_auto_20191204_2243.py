# Generated by Django 2.2.6 on 2019-12-04 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0003_auto_20191202_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vkauth',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='vkauth',
            old_name='surname',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='vkauth',
            name='code',
        ),
    ]
