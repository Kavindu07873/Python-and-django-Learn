# Generated by Django 4.2.2 on 2023-07-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_remove_customerapi_email_remove_customerapi_paasword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('email', models.EmailField(default='xample@example.com', max_length=100, unique=True)),
                ('conNo', models.IntegerField()),
                ('nic', models.IntegerField()),
                ('paasword', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerApi',
        ),
    ]
