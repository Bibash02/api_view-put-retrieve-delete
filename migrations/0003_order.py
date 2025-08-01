# Generated by Django 5.2.3 on 2025-06-21 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0002_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('P', 'pending'), ('D', 'delevired'), ('C', 'cancled')], default='P', max_length=1)),
                ('payment', models.CharField(choices=[('P', 'payed'), ('U', 'unpayed')], default='U', max_length=1)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
