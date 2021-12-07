# Generated by Django 3.2.10 on 2021-12-13 01:51

from django.db import migrations
from django.utils import timezone

def create_default_session(apps, schema_editor):
    Session = apps.get_model("RadioActiv8", "Session")
    db_alias = schema_editor.connection.alias

    now = timezone.now()
    Session.objects.using(db_alias).create(name='DEFAULT SESSION', start_time=now, end_time=now)


def delete_default_session(apps, schema_editor):
    Session = apps.get_model("RadioActiv8", "Session")
    db_alias = schema_editor.connection.alias

    Session.objects.using(db_alias).filter(name='DEFAULT SESSION').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('RadioActiv8', '0003_create_session_model'),
    ]

    operations = [
        migrations.RunPython(create_default_session, delete_default_session)
    ]
