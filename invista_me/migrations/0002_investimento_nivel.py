# Generated by Django 4.0.4 on 2022-05-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investimento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]