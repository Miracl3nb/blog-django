# Generated by Django 4.2.1 on 2023-06-05 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_delete_posteos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='content',
            new_name='description',
        ),
    ]