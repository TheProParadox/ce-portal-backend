# Generated by Django 4.1 on 2022-09-07 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_rename_competitions_competition_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='competitions',
            new_name='competition',
        ),
    ]
