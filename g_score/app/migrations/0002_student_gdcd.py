# Generated by Django 4.2.3 on 2024-12-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gdcd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
