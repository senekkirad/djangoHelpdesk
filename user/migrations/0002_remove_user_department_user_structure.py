# Generated by Django 4.2.6 on 2023-10-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.AddField(
            model_name='user',
            name='structure',
            field=models.IntegerField(choices=[(1, 'DADIGITALL'), (2, 'CHALENGE DISTRIBUTION')], default=1, verbose_name='structure'),
            preserve_default=False,
        ),
    ]
