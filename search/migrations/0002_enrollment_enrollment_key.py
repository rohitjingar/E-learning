# Generated by Django 4.1.7 on 2023-05-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='enrollment_key',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]