# Generated by Django 2.1 on 2019-04-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0047_auto_20190423_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlistings',
            name='pimg',
            field=models.FileField(blank=True, default='default.jpg', null=True, upload_to='product_media'),
        ),
    ]