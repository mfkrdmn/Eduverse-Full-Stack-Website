# Generated by Django 4.0.5 on 2022-07-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]