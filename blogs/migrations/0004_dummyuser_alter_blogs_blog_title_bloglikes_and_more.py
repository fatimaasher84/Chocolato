# Generated by Django 4.2.2 on 2023-08-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='BlogLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.dummyuser')),
            ],
        ),
        migrations.AddField(
            model_name='blogs',
            name='blog_likes',
            field=models.ManyToManyField(related_name='blog_posts', through='blogs.BlogLikes', to='blogs.dummyuser'),
        ),
    ]
