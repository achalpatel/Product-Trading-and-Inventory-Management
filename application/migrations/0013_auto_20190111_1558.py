# Generated by Django 2.1.4 on 2019-01-11 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20190111_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListings',
            fields=[
                ('plistId', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stId', models.AutoField(primary_key=True, serialize=False)),
                ('sQty', models.IntegerField()),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
            ],
        ),
        migrations.CreateModel(
            name='StockDetail',
            fields=[
                ('stdId', models.AutoField(primary_key=True, serialize=False)),
                ('pNo', models.DecimalField(decimal_places=5, max_digits=10)),
                ('stId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('tId', models.AutoField(primary_key=True, serialize=False)),
                ('s_uId', models.IntegerField()),
                ('b_uId', models.IntegerField()),
                ('tDate', models.DateTimeField(auto_now_add=True)),
                ('tQty', models.IntegerField()),
                ('pId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Product')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetail',
            fields=[
                ('tdId', models.AutoField(primary_key=True, serialize=False)),
                ('stdId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.StockDetail')),
                ('tId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uId', models.AutoField(primary_key=True, serialize=False)),
                ('uName', models.CharField(max_length=20)),
                ('uPass', models.CharField(max_length=20)),
                ('is_whole', models.BooleanField()),
                ('is_retail', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='uId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Users'),
        ),
        migrations.AddField(
            model_name='productlistings',
            name='uId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Users'),
        ),
    ]