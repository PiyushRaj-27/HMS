# Generated by Django 4.1.4 on 2023-10-29 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_patients_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='img',
            field=models.ImageField(upload_to='data/images'),
        ),
    ]
