# Generated by Django 4.1.5 on 2023-01-11 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_at',
            new_name='category_created_at',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='modified_at',
            new_name='category_modified_at',
        ),
    ]