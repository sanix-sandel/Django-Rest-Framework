# Generated by Django 3.0.7 on 2020-07-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20200701_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerscore',
            name='score_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
