# Generated by Django 4.2.2 on 2023-07-02 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_service'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
    ]