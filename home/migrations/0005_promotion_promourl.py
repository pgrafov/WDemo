# Generated by Django 2.0.6 on 2018-06-13 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20180613_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=60)),
                ('price', models.FloatField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PromoUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=60, unique=True)),
                ('promopage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.PromoPage')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Promotion')),
            ],
        ),
    ]
