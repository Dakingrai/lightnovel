# Generated by Django 3.0.5 on 2020-04-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0008_auto_20200417_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='chapter_content',
            field=models.TextField(null=True),
        ),
    ]
