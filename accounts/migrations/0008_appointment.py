# Generated by Django 4.0.4 on 2022-06-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_doctor_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Mobil', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('date', models.DateField()),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('time', models.TimeField()),
            ],
        ),
    ]