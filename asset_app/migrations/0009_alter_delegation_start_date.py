# Generated by Django 3.2.19 on 2023-08-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_app', '0008_auto_20230824_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegation',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
