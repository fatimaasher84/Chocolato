# Generated by Django 4.2.2 on 2023-07-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choco', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choco',
            name='ch_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='chimages/'),
        ),
    ]
