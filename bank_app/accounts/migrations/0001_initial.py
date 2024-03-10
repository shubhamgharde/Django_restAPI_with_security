# Generated by Django 3.2.14 on 2022-12-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ifscode', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'BANK_MASTER',
            },
        ),
        migrations.CreateModel(
            name='Cust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bank')),
            ],
            options={
                'db_table': 'CUST_MASTER',
            },
        ),
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('bank', models.ManyToManyField(to='accounts.Cust')),
            ],
            options={
                'db_table': 'ADDRESS _MASTER',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('balance', models.FloatField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.bank')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.cust')),
            ],
            options={
                'db_table': 'ACCOUNT_MASTER',
            },
        ),
    ]