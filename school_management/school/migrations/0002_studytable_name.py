# Generated by Django 2.2.6 on 2019-10-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studytable',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
