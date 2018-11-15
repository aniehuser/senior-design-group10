# Generated by Django 2.1.3 on 2018-11-14 00:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('yw_db', '0003_auto_20181113_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='last_modified_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 14, 0, 1, 36, 619802, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='run',
            name='version_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Version'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parent_tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='yw_db.Tag'),
        ),
        migrations.AlterField(
            model_name='tagfile',
            name='file_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.File'),
        ),
        migrations.AlterField(
            model_name='tagfile',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Tag'),
        ),
        migrations.AlterField(
            model_name='tagrun',
            name='run_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Run'),
        ),
        migrations.AlterField(
            model_name='tagrun',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Tag'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Tag'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='version_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Version'),
        ),
        migrations.AlterField(
            model_name='tagworkflow',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Tag'),
        ),
        migrations.AlterField(
            model_name='tagworkflow',
            name='workflow_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Workflow'),
        ),
        migrations.AlterField(
            model_name='version',
            name='workflow_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yw_db.Workflow'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
