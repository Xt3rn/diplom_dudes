# Generated by Django 2.2.19 on 2025-07-01 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom_spo', '0005_auto_20250630_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diplom',
            name='ser_number',
            field=models.CharField(default='Введите данные', help_text='Введите номер серии', max_length=15, verbose_name='Номер серии'),
        ),
    ]
