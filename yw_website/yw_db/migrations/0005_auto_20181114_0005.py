# Generated by Django 2.1.3 on 2018-11-14 00:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yw_db', '0004_auto_20181114_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='run',
            old_name='version_id',
            new_name='version',
        ),
        migrations.RenameField(
            model_name='runfile',
            old_name='file_id',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='runfile',
            old_name='run_id',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='parent_tag_id',
            new_name='parent_tag',
        ),
        migrations.RenameField(
            model_name='tagfile',
            old_name='file_id',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='tagfile',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tagrun',
            old_name='run_id',
            new_name='run',
        ),
        migrations.RenameField(
            model_name='tagrun',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tagversion',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tagversion',
            old_name='version_id',
            new_name='version',
        ),
        migrations.RenameField(
            model_name='tagworkflow',
            old_name='tag_id',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='tagworkflow',
            old_name='workflow_id',
            new_name='workflow',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='workflow_id',
            new_name='workflow',
        ),
        migrations.RenameField(
            model_name='workflow',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='file',
            name='last_modified_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 0, 5, 41, 356883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tagworkflow',
            name='workflow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Workflow'),
        ),
        migrations.AlterField(
            model_name='version',
            name='workflow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Workflow'),
        ),
    ]