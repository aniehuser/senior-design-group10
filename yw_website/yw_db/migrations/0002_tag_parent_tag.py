# Generated by Django 2.1.1 on 2018-11-11 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yw_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='parent_tag',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='yw_db.Tag'),
        ),
    ]