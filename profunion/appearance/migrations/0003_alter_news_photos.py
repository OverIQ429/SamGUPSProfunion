# Generated by Django 5.0.4 on 2024-05-08 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0002_alter_news_options_news_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photos',
            field=models.ImageField(upload_to='images'),
        ),
    ]