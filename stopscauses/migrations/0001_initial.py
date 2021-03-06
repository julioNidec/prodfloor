# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tier1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_one_cause', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'First Level Causes',
                'verbose_name': 'First Level Cause',
            },
        ),
        migrations.CreateModel(
            name='Tier2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_two_cause', models.CharField(max_length=200)),
                ('tier_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stopscauses.Tier1')),
            ],
            options={
                'verbose_name_plural': 'Second Level Causes',
                'verbose_name': 'Second Level Cause',
            },
        ),
        migrations.CreateModel(
            name='Tier3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_three_cause', models.CharField(max_length=200)),
                ('tier_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stopscauses.Tier2')),
            ],
            options={
                'verbose_name_plural': 'Third Level Causes',
                'verbose_name': 'Third Level Cause',
            },
        ),
    ]
