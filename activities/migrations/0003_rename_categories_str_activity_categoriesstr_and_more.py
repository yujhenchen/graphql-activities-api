# Generated by Django 5.1.7 on 2025-05-16 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_activity_categories_str_activity_seasons_str'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='categories_str',
            new_name='categoriesstr',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='seasons_str',
            new_name='seasonsstr',
        ),
    ]
