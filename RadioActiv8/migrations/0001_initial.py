# Generated by Django 3.2.9 on 2021-11-14 04:44

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Intelligence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1024)),
                ('answer', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gps_location', django.contrib.gis.db.models.fields.PointField(blank=True, default=django.contrib.gis.geos.point.Point(144.6376, -36.49197), srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Patrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('location_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RadioActiv8.location')),
                ('location_name', models.CharField(max_length=128)),
                ('channel', models.IntegerField(blank=True, null=True)),
            ],
            bases=('RadioActiv8.location',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=1024, null=True)),
                ('intelligence_answered_correctly', models.BooleanField(default=False)),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Destination', to='RadioActiv8.location')),
                ('intelligence_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RadioActiv8.intelligence')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RadioActiv8.location')),
                ('patrol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RadioActiv8.patrol')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('radio_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RadioActiv8.radio')),
                ('min_patrols', models.IntegerField(blank=True, null=True)),
                ('max_patrols', models.IntegerField(blank=True, null=True)),
                ('activity_type', models.CharField(blank=True, choices=[('R', 'Reading data'), ('S', 'Self-directed'), ('F', 'Facilitated')], default='S', max_length=1)),
            ],
            bases=('RadioActiv8.radio',),
        ),
        migrations.AddField(
            model_name='intelligence',
            name='base',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RadioActiv8.base'),
        ),
    ]
