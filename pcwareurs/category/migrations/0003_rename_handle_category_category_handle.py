# Generated by Django 4.1.5 on 2023-01-11 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_created_at_category_category_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='handle',
            new_name='category_handle',
        ),
    ]
