# Generated by Django 2.2.6 on 2019-10-30 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_studytable_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studytable',
            name='name',
        ),
    ]