# Generated by Django 5.0.7 on 2024-08-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('nickname', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=20, unique=True)),
                ('pwd', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'accounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('boardname', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postid', models.CharField(db_column='postID', max_length=64, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('contents', models.TextField()),
                ('createdtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
    ]
