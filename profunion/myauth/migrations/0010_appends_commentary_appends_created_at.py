# Generated by Django 5.0.4 on 2024-05-12 07:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0009_profile_is_union_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='appends',
            name='commentary',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='appends',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
