# Generated by Django 4.2.1 on 2023-06-22 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_businesstype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(default='UNKNOWN', max_length=200)),
                ('detail', models.CharField(default='UNKNOWN', max_length=200)),
                ('title', models.CharField(default='UNKNOWN', max_length=200)),
                ('position_start', models.CharField(default='UNKNOWN', max_length=200)),
                ('position_end', models.CharField(default='UNKNOWN', max_length=200)),
                ('date_start', models.DateField(blank=True, null=True)),
                ('date_end', models.DateField(blank=True, null=True)),
                ('budget', models.FloatField(default=0)),
                ('total_cost', models.FloatField(default=0)),
                ('places', models.TextField(default='UNKNOWN')),
                ('permission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(default='UNKNOWN', max_length=200)),
                ('name', models.CharField(default='UNKNOWN', max_length=200)),
                ('detail', models.CharField(default='UNKNOWN', max_length=200)),
                ('price', models.FloatField(default=0)),
                ('lat', models.CharField(default='UNKNOWN', max_length=25)),
                ('lng', models.CharField(default='UNKNOWN', max_length=25)),
                ('district', models.CharField(default='UNKNOWN', max_length=200)),
                ('province', models.CharField(default='UNKNOWN', max_length=200)),
                ('timeOpen', models.TimeField(blank=True, null=True)),
                ('timeClose', models.TimeField(blank=True, null=True)),
                ('website', models.CharField(default='UNKNOWN', max_length=200)),
                ('pinPhotograph', models.TextField(blank=True, null=True)),
                ('pinCheckIn', models.TextField(blank=True, null=True)),
                ('recomendStatus', models.IntegerField(default=0)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_type', to='watchlist_app.businesstype')),
            ],
        ),
    ]
