# Generated by Django 2.2 on 2019-04-22 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190417_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='table',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps', to='core.Solution'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='core.Solution'),
        ),
        migrations.CreateModel(
            name='MappedField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=30)),
                ('entity_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='core.EntityMap')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappings', to='core.Field')),
            ],
        ),
        migrations.AddField(
            model_name='entitymap',
            name='app',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='core.App'),
        ),
        migrations.AddField(
            model_name='entitymap',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='core.Entity'),
        ),
    ]
