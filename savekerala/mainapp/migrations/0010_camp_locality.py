# Generated by Django 2.1 on 2018-08-21 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_locality_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='locality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Locality'),
        ),
    ]
