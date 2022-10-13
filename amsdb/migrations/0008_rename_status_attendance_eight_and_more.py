# Generated by Django 4.1.1 on 2022-10-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amsdb', '0007_alter_subject_sub_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='status',
            new_name='eight',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='attendance_student',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='subject_code',
        ),
        migrations.AddField(
            model_name='attendance',
            name='fifth',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='first',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='fourth',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='overall',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='second',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='seveen',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='sixth',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='third',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
