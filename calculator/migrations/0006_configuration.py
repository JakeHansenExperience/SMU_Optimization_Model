# Generated by Django 3.0.6 on 2020-06-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_layout_plantresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration_name', models.CharField(max_length=255)),
            ],
        ),
    ]
