# Generated by Django 2.1.4 on 2019-01-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_auto_20190117_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='s_uId',
            field=models.CharField(max_length=50),
        ),
    ]
