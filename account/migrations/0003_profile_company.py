# Generated by Django 3.2.19 on 2023-08-23 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0001_initial'),
        ('account', '0002_alter_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset_app.company'),
        ),
    ]