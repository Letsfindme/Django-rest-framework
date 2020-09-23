# Generated by Django 2.2.5 on 2019-10-29 20:18

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191029_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='post',
            name='starCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=core.models.post_image_file_path),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='creationDate',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='firstConnection',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastConnection',
            field=models.DateField(null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='updatedDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PostRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('imageRef', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]