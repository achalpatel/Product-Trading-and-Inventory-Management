# Generated by Django 2.1.4 on 2019-01-16 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0020_auto_20190116_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='pId',
        ),
        migrations.AddField(
            model_name='stock',
            name='pListId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.ProductListings'),
        ),
    ]
