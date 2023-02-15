# Generated by Django 3.2.16 on 2023-02-15 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20230213_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=3)),
                ('students', models.ManyToManyField(to='students.Student')),
            ],
        ),
    ]