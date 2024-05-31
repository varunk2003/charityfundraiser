# Generated by Django 3.0.5 on 2023-10-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundraiser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.AddField(
            model_name='log',
            name='signins',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]