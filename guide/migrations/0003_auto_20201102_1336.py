# Generated by Django 3.1.2 on 2020-11-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_auto_20201031_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='adress',
            field=models.TextField(verbose_name='Адрес'),
        ),
    ]