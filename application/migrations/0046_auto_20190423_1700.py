# Generated by Django 2.1 on 2019-04-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0045_auto_20190304_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlistings',
            name='pimg',
            field=models.FileField(blank=True, default='C:/Users/achal/Desktop/New folder (2)/default.jpg', null=True, upload_to='product_media'),
        ),
    ]
