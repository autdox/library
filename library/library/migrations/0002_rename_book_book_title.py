# Generated by Django 4.0.3 on 2022-10-11 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book',
            new_name='title',
        ),
    ]