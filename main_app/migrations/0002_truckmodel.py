# Generated by Django 4.2.2 on 2023-07-02 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TruckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('max_speed', models.IntegerField(default=0)),
                ('truck_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='truck_model', to='main_app.truckbrand')),
            ],
        ),
    ]