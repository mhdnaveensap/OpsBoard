# Generated by Django 2.0 on 2017-12-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmaster', '0006_auto_20171229_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_active',
            field=models.BooleanField(default=True),
        ),
    ]
