# Generated by Django 3.1.1 on 2022-11-15 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=1000)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaExpressPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckoutRequestID', models.CharField(blank=True, max_length=50, null=True)),
                ('MerchantRequestID', models.CharField(blank=True, max_length=20, null=True)),
                ('ResultCode', models.IntegerField(blank=True, null=True)),
                ('ResultDesc', models.CharField(blank=True, max_length=120, null=True)),
                ('Amount', models.FloatField(blank=True, null=True)),
                ('MpesaReceiptNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('Balance', models.CharField(blank=True, max_length=12, null=True)),
                ('TransactionDate', models.DateTimeField(blank=True, null=True)),
                ('PhoneNumber', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaTillPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionType', models.CharField(blank=True, max_length=12, null=True)),
                ('TransID', models.CharField(blank=True, max_length=12, null=True)),
                ('TransTime', models.CharField(blank=True, max_length=14, null=True)),
                ('TransAmount', models.CharField(blank=True, max_length=12, null=True)),
                ('BusinessShortCode', models.CharField(blank=True, max_length=6, null=True)),
                ('BillRefNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('InvoiceNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('OrgAccountBalance', models.CharField(blank=True, max_length=12, null=True)),
                ('ThirdPartyTransID', models.CharField(blank=True, max_length=20, null=True)),
                ('MSISDN', models.CharField(blank=True, max_length=12, null=True)),
                ('FirstName', models.CharField(blank=True, max_length=20, null=True)),
                ('MiddleName', models.CharField(blank=True, max_length=20, null=True)),
                ('LastName', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('discharged', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='cafeteria.OrderItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]