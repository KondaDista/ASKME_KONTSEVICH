# Generated by Django 5.1.2 on 2024-11-12 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_profile_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id_answer',
        ),
        migrations.AddField(
            model_name='answer',
            name='id_question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='application.question'),
            preserve_default=False,
        ),
    ]
