# Generated by Django 3.2.5 on 2023-09-21 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock_level', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping_mall.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.sale')),
            ],
        ),
        migrations.AddField(
            model_name='sale',
            name='products',
            field=models.ManyToManyField(through='shopping_mall.SaleItem', to='shopping_mall.Product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.store'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping_mall.product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='purchase_history',
            field=models.ManyToManyField(through='shopping_mall.Purchase', to='shopping_mall.Product'),
        ),
    ]
