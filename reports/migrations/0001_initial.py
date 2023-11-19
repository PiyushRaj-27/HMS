# Generated by Django 4.1.4 on 2023-11-19 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('rep', models.FileField(upload_to='data/reports')),
                ('pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
