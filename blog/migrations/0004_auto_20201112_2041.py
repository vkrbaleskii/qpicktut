# Generated by Django 3.1.3 on 2020-11-12 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201111_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='post_body',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='post_title',
            new_name='title',
        ),
    ]
