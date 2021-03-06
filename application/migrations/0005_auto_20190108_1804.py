# Generated by Django 2.1.4 on 2019-01-08 12:34

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('application', '0004_auto_20190108_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subCatId',
        ),
        migrations.RemoveField(
            model_name='productlistings',
            name='pId',
        ),
        migrations.RemoveField(
            model_name='productlistings',
            name='uId',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='pId',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='uId',
        ),
        migrations.RemoveField(
            model_name='stockdetail',
            name='stId',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='catId',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='pId',
        ),
        migrations.RemoveField(
            model_name='transactiondetail',
            name='stdId',
        ),
        migrations.RemoveField(
            model_name='transactiondetail',
            name='tId',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductListings',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.DeleteModel(
            name='StockDetail',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='TransactionDetail',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
