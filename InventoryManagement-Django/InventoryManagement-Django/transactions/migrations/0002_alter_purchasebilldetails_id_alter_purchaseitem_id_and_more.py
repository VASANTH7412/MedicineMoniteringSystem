# Generated by Django 5.1.7 on 2025-03-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasebilldetails',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='salebilldetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='saleitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
