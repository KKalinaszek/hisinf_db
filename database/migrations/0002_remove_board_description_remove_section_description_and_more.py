# Generated by Django 4.2.1 on 2023-05-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='description',
        ),
        migrations.RemoveField(
            model_name='section',
            name='description',
        ),
        migrations.RemoveField(
            model_name='section',
            name='section',
        ),
        migrations.AddField(
            model_name='section',
            name='text',
            field=models.TextField(default='', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='section',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='section',
            name='no',
            field=models.PositiveIntegerField(),
        ),
    ]
