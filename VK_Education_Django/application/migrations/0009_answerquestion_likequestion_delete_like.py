# Generated by Django 5.1.2 on 2024-11-12 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerQuestion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.answer')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.profile')),
            ],
            options={
                'unique_together': {('id_answer', 'id_user')},
            },
        ),
        migrations.CreateModel(
            name='LikeQuestion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.question')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.profile')),
            ],
            options={
                'unique_together': {('id_question', 'id_user')},
            },
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
