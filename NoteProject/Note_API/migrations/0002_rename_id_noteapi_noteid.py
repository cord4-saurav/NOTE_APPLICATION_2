# Generated by Django 3.2.9 on 2022-05-17 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Note_API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noteapi',
            old_name='ID',
            new_name='NoteID',
        ),
    ]