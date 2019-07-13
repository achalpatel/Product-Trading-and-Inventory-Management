# Generated by Django 2.1.4 on 2019-01-23 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0033_auto_20190123_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=50)),
                ('catImg', models.FileField(blank=True, null=True, upload_to='cat_media')),
                ('isDisplay', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manuName', models.CharField(max_length=50)),
                ('manuContact', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(db_index=True, max_length=50)),
                ('catId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductListings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('s_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.IntegerField()),
                ('pdDescription', models.CharField(blank=True, max_length=100, null=True)),
                ('pimg', models.FileField(blank=True, null=True, upload_to='product_media')),
                ('manuName', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Manufacturer')),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
                ('uName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sQty', models.IntegerField()),
                ('pListId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.ProductListings')),
                ('uName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pNo', models.DecimalField(decimal_places=5, max_digits=10)),
                ('stId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCatName', models.CharField(max_length=50)),
                ('SubCatImg', models.FileField(blank=True, null=True, upload_to='Subcat_media')),
                ('isDisplay', models.BooleanField(default=True)),
                ('catId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_uId', models.CharField(max_length=50)),
                ('b_uId', models.CharField(max_length=50)),
                ('tDate', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tQty', models.IntegerField()),
                ('pListId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.ProductListings')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.StockDetail')),
                ('tId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subCatId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.SubCategory'),
        ),
    ]
