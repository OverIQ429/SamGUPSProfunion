# Generated by Django 5.0.4 on 2024-05-09 13:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0006_description_remove_appends_discription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=10)),
                ('course', models.IntegerField()),
                ('faculty', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+79999999999'. Up to 10 digits allowed.", regex='^\\+7\\d{10}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myauth.allgroups'),
        ),
    ]
