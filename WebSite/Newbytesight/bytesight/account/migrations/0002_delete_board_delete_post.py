# Generated by Django 5.0.7 on 2024-08-23 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]