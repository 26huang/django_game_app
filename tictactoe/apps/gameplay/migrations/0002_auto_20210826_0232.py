# Generated by Django 2.2.6 on 2021-08-26 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='move',
            name='game',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Move',
        ),
    ]
