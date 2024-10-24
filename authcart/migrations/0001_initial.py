# Generated by Django 5.1.2 on 2024-10-12 07:26

from django.db import migrations, models
from django.core.validators import RegexValidator, MinLengthValidator

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('desc', models.TextField(max_length=500)),
                ('phonenumber', models.CharField(
                    max_length=10,
                    validators=[
                        RegexValidator(regex='^\d{10}$', message='Phone number must be 10 digits long'),
                        MinLengthValidator(10),
                    ]
                )),
            ],
        ),
    ]
