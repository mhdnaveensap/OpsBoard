# Generated by Django 2.0 on 2018-01-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0009_taskmaster_istasktobeperformed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmaster',
            name='istasktobeperformed',
            field=models.BooleanField(default=False),
        ),
    ]
