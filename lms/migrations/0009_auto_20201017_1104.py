# Generated by Django 3.1.2 on 2020-10-17 05:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0008_auto_20201016_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='creator',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reported',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='lms.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sno',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Replies',
        ),
    ]
