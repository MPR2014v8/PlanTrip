# Generated by Django 4.2.1 on 2023-06-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_watchlist_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='UNKNOWN', max_length=200)),
                ('detail', models.CharField(default='UNKNOWN', max_length=200)),
            ],
        ),
    ]
