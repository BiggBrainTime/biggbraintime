# Generated by Django 3.1.2 on 2020-10-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
