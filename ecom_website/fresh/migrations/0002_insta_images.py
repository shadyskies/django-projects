# Generated by Django 3.1.5 on 2021-06-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insta_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.URLField(max_length=128)),
            ],
        ),
    ]