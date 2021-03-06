# Generated by Django 2.1.4 on 2018-12-31 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('aID', models.AutoField(primary_key=True, serialize=False)),
                ('uName', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=15)),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('DOJ', models.DateTimeField(auto_now_add=True)),
                ('contactNo', models.CharField(max_length=20)),
                ('eMail', models.EmailField(max_length=30)),
                ('logo', models.FileField(blank=True, null=True, upload_to='adminLogo_media')),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('aId', models.AutoField(primary_key=True, serialize=False)),
                ('atName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttributes',
            fields=[
                ('paId', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.IntegerField()),
                ('aID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Attributes')),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('piId', models.AutoField(primary_key=True, serialize=False)),
                ('images', models.FileField(blank=True, null=True, upload_to='product_image')),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('sID', models.AutoField(primary_key=True, serialize=False)),
                ('DOS', models.DateTimeField(auto_now_add=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('sdId', models.AutoField(primary_key=True, serialize=False)),
                ('Qty', models.IntegerField()),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
                ('sId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Sale')),
            ],
        ),
        migrations.CreateModel(
            name='SaleDetailBatch',
            fields=[
                ('sdbId', models.AutoField(primary_key=True, serialize=False)),
                ('sPrice', models.IntegerField()),
                ('batchPurDetailsId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.BatchPurchaseDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stockId', models.AutoField(primary_key=True, serialize=False)),
                ('DOS', models.DateTimeField(auto_now_add=True)),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('sdId', models.AutoField(primary_key=True, serialize=False)),
                ('sIn', models.IntegerField()),
                ('sOut', models.IntegerField()),
                ('stockId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Stock')),
            ],
        ),
    ]
