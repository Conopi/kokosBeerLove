# Generated by Django 5.1.1 on 2024-10-13 23:58

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('Обработан', 'Обработан'), ('В ожидании', 'В ожидании')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=1000)),
                ('discount', models.PositiveIntegerField(default=0)),
                ('category', models.CharField(choices=[('Одежда', 'Одежда'), ('Аксессуары', 'Аксессуары')], max_length=255)),
                ('url_images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, default=list, size=None)),
            ],
            options={
                'db_table': 'shop_products',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_microservice_app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_microservice_app.product')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='shop_microservice_app.OrderItem', to='shop_microservice_app.product'),
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='shop_microservice_app.product')),
            ],
            options={
                'db_table': 'product_sizes',
                'unique_together': {('product', 'size')},
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_microservice_app.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_microservice_app.productsize')),
            ],
            options={
                'db_table': 'cart_items',
            },
        ),
    ]
