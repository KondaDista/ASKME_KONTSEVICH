# Generated by Django 5.1.2 on 2024-11-13 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_alter_dislikeanswer_id_alter_dislikequestion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]