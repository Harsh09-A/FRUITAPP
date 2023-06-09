# Generated by Django 3.2.12 on 2022-05-14 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addtocart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(max_length=100)),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_Price', models.CharField(max_length=100)),
                ('Product_Discount_price', models.CharField(max_length=100)),
                ('Product_Unit', models.CharField(default='', max_length=100)),
                ('Product_img', models.CharField(default='', max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_Category', models.CharField(max_length=100)),
                ('Product_Short_Description', models.TextField(max_length=100)),
                ('Product_Full_Description', models.TextField(max_length=100)),
                ('Product_Price', models.CharField(max_length=100)),
                ('Product_Discount_price', models.CharField(max_length=100)),
                ('Product_Tag', models.CharField(max_length=500)),
                ('Product_Seo', models.CharField(max_length=500)),
                ('Product_Unit', models.CharField(default='', max_length=100)),
                ('Product_img', models.ImageField(max_length=200, upload_to='Products')),
                ('Product_slide', models.ImageField(max_length=200, upload_to='Products')),
                ('Product_slide2', models.ImageField(max_length=200, upload_to='Products')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('subject', models.CharField(default='', max_length=100)),
                ('qmessage', models.CharField(default='', max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(max_length=100)),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_Price', models.CharField(max_length=100)),
                ('Product_Discount_price', models.CharField(max_length=100)),
                ('Product_Unit', models.CharField(default='', max_length=100)),
                ('Product_img', models.CharField(default='', max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]