# Generated by Django 4.1.7 on 2023-05-11 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='certifications',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='completed_courses',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='learning_interests',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skill_set',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(blank=True, max_length=122),
        ),
    ]