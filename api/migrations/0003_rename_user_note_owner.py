# Generated by Django 4.1.7 on 2023-02-16 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_note_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='user',
            new_name='owner',
        ),
    ]