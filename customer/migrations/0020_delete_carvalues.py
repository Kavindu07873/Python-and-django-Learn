# Generated by Django 4.2.2 on 2023-07-10 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_carvalues_delete_cardetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarValues',
        ),
    ]