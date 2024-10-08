# Generated by Django 5.1.1 on 2024-09-07 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='bank',
        ),
        migrations.AddField(
            model_name='branch',
            name='bank_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='myapp.bank'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=49),
        ),
    ]
