# Generated by Django 5.0.4 on 2024-05-08 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='photos',
            field=models.ImageField(default='\\default_picures\x04ccc0482-726a-4a8b-990b-014edd4d4774.jpg', upload_to='images'),
        ),
    ]
