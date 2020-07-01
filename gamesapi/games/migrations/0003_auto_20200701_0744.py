# Generated by Django 3.0.7 on 2020-07-01 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20200630_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=50)),
                ('genre', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='PlayScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('score_date', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='games.Player')),
            ],
            options={
                'ordering': ('-score',),
            },
        ),
        migrations.AlterField(
            model_name='game',
            name='game_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.GameCategory'),
        ),
    ]
