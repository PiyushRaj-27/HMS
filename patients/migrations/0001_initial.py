# Generated by Django 4.1.4 on 2023-09-10 08:51

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
            name='patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('marr', models.CharField(max_length=10)),
                ('empl', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='data/images')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
