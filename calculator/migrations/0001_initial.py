# Generated by Django 3.0.6 on 2020-05-19 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('workers', models.IntegerField(default=0)),
                ('shifts', models.IntegerField(default=0)),
                ('wages', models.DecimalField(decimal_places=2, max_digits=6)),
                ('labor_dollar_hr', models.DecimalField(decimal_places=2, max_digits=6)),
                ('energy_dollar_hr', models.DecimalField(decimal_places=2, max_digits=6)),
                ('variable_dollar_hr', models.DecimalField(decimal_places=2, max_digits=6)),
                ('interior_heavy_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insulated_glass_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laminated_complex_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laminated_simple_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specialty_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_hr_month', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_hr_shift', models.DecimalField(decimal_places=2, max_digits=10)),
                ('days', models.IntegerField(default=0)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Plant')),
            ],
        ),
    ]
