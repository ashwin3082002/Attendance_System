# Generated by Django 4.1.1 on 2022-11-29 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amsdb', '0002_faculty_detail_class_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='stu_atten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('roll', models.CharField(max_length=255)),
                ('total_present', models.CharField(max_length=255)),
                ('total_absent', models.CharField(max_length=255)),
                ('percentage', models.CharField(max_length=255)),
                ('date_gen', models.DateField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]