# Generated by Django 4.1.4 on 2023-11-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patients_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='credit',
            field=models.CharField(default='100', max_length=8),
        ),
    ]