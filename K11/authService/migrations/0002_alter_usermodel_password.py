# Generated by Django 4.1.7 on 2023-04-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.BinaryField(max_length=100),
        ),
    ]