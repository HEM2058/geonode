# Generated by Django 3.2.18 on 2023-06-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0040_auto_20230627_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadsizelimit',
            name='max_size',
            field=models.PositiveBigIntegerField(default=5368709120, help_text='The maximum file size allowed for upload (bytes).'),
        ),
    ]