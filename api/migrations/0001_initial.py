# Generated by Django 3.1.2 on 2020-10-30 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address_street', models.CharField(max_length=255)),
                ('address_suite', models.CharField(max_length=255)),
                ('address_city', models.CharField(max_length=255)),
                ('address_zipcode', models.CharField(max_length=255)),
                ('address_geo_lat', models.FloatField()),
                ('address_geo_lng', models.FloatField()),
                ('company_name', models.CharField(max_length=255)),
                ('company_catch_phrase', models.CharField(max_length=255)),
                ('company_bs', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'User',
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='api.usermodel')),
            ],
            options={
                'verbose_name': 'Post',
                'db_table': 'posts',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='api.postmodel')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='api.usermodel')),
            ],
            options={
                'verbose_name': 'Comment',
                'db_table': 'comments',
            },
        ),
    ]
