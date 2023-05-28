# Generated by Django 4.2.1 on 2023-05-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_remove_board_description_remove_section_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=25, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='question_id',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='board',
            new_name='board_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.AddField(
            model_name='question',
            name='no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='page',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], default='A', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='no',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='no',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
