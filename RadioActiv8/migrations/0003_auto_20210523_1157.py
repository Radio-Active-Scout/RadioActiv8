# Generated by Django 3.2.3 on 2021-05-23 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RadioActiv8', '0002_auto_20210514_1801'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterModelOptions(
            name='queue',
            options={'ordering': ['sequence']},
        ),
        migrations.AddField(
            model_name='base',
            name='activity_type',
            field=models.CharField(blank=True, choices=[('R', 'Reading data'), ('S', 'Self-directed'), ('F', 'Facilitated')], max_length=1),
        ),
        migrations.AddField(
            model_name='base',
            name='channel',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
