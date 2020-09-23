# Generated by Django 2.2.5 on 2019-10-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191029_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='imageRef',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]