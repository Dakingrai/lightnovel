# Generated by Django 3.0.5 on 2020-04-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0006_auto_20200417_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='chapter_content',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='chapter',
            field=models.TextField(null=True),
        ),
    ]