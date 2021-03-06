# Generated by Django 3.0.6 on 2020-05-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20200519_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demand_name', models.CharField(max_length=255)),
                ('interior_heavy_demand', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insulated_glass_demand', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laminated_simple_demand', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laminated_complex_demand', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specialty_demand', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(max_length=255)),
                ('function_id', models.IntegerField()),
            ],
        ),
    ]
