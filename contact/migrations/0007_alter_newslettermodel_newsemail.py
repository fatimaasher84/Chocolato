# Generated by Django 4.2.2 on 2023-08-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_newslettermodel_newsemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettermodel',
            name='newsEmail',
            field=models.EmailField(max_length=254),
        ),
    ]
