# Generated by Django 4.0.3 on 2022-10-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_comment_delete_models'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentId',
        ),
        migrations.AddField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]