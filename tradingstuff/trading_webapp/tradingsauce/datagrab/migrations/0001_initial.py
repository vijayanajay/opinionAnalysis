# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 15:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('openPrice', models.FloatField()),
                ('highPrice', models.FloatField()),
                ('lowPrice', models.FloatField()),
                ('closePrice', models.FloatField()),
                ('wap', models.FloatField()),
                ('numberOfShares', models.IntegerField()),
                ('numberOfTrades', models.IntegerField()),
                ('totalTurnover', models.FloatField()),
                ('spreadHighLow', models.FloatField()),
                ('spreadCloseOpen', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockSymbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('symbol', models.CharField(max_length=10)),
                ('tickerNumber', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datagrab.StockSymbol'),
        ),
    ]
