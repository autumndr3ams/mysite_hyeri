# Generated by Django 3.0.6 on 2020-05-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydiary', '0003_content_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='file',
            field=models.FileField(blank=True, upload_to='documents/%Y.%m'),
        ),
    ]
