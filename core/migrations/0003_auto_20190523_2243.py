# Generated by Django 2.2 on 2019-05-23 22:43

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190509_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='field_type',
            field=models.CharField(choices=[(core.models.FIELD_TYPES('char'), 'char'), (core.models.FIELD_TYPES('bool'), 'bool'), (core.models.FIELD_TYPES('int'), 'int'), (core.models.FIELD_TYPES('dec'), 'dec'), (core.models.FIELD_TYPES('timestamp'), 'timestamp'), (core.models.FIELD_TYPES('UUID'), 'UUID')], max_length=12),
        ),
    ]