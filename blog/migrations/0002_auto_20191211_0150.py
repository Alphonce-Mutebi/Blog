# Generated by Django 2.2.7 on 2019-12-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Blank', max_length=100),
        ),
    ]
