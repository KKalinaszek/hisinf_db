# Generated by Django 4.0.5 on 2023-06-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_rename_file_mp3file_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=25, unique=True)),
                ('description', models.TextField(default='', max_length=250, unique=True)),
                ('points', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Prizes',
            },
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name_plural': 'Players'},
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=25, unique=True)),
                ('prizes', models.ManyToManyField(related_name='events', to='database.prize')),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]
