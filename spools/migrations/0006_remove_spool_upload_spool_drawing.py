# Generated by Django 4.0.1 on 2022-01-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spools', '0005_spool_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spool',
            name='upload',
        ),
        migrations.AddField(
            model_name='spool',
            name='drawing',
            field=models.FileField(default='na', upload_to='drawings/'),
            preserve_default=False,
        ),
    ]
