# Generated by Django 3.2.10 on 2022-01-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='passwords',
            new_name='password',
        ),
    ]
