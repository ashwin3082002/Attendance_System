# Generated by Django 4.1.1 on 2022-10-12 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amsdb', '0002_course_student_detail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('class_id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('sem', models.CharField(max_length=120)),
                ('year', models.CharField(max_length=120)),
                ('section', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('sub_id', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsdb.classes')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsdb.faculty_detail')),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsdb.course')),
            ],
        ),
        migrations.RenameField(
            model_name='student_detail',
            old_name='sem',
            new_name='reg_no',
        ),
        migrations.RemoveField(
            model_name='student_detail',
            name='section',
        ),
        migrations.RemoveField(
            model_name='student_detail',
            name='year',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attendance_student',
            field=models.CharField(choices=[('A', 'ABSENT'), ('P', 'PRESENT'), ('OD', 'ONDUTY')], default='A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('class_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsdb.classes')),
                ('eight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Eight_Hour', to='amsdb.subject')),
                ('fifth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fifth_Hour', to='amsdb.subject')),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='First_Hour', to='amsdb.subject')),
                ('fourth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fourth_Hour', to='amsdb.subject')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Second_Hour', to='amsdb.subject')),
                ('seveen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Seveen_Hour', to='amsdb.subject')),
                ('sixth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Sixth_Hour', to='amsdb.subject')),
                ('third', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Third_Hour', to='amsdb.subject')),
            ],
        ),
        migrations.AddField(
            model_name='attendance',
            name='s_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='amsdb.classes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='subject_code',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='amsdb.subject'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student_detail',
            name='s_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='amsdb.classes'),
            preserve_default=False,
        ),
    ]
