# Generated by Django 2.1.4 on 2019-01-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20190108_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='uPass',
            field=models.CharField(default='', max_length=20),
        ),
    ]
