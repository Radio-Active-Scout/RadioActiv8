# Generated by Django 4.0 on 2021-12-29 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("RadioActiv8", "0018_alter_base_options_alter_gpstracker_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="home_base",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="is_home_base",
                to="RadioActiv8.base",
            ),
        ),
    ]
