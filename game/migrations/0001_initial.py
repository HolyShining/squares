# Generated by Django 2.2.2 on 2019-06-11 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.IntegerField()),
                ('squares', models.IntegerField()),
                ('cards', models.IntegerField()),
                ('sequence', models.CharField(max_length=79)),
                ('deck', models.TextField(max_length=600)),
            ],
            options={
                'db_table': 'game_history',
                'ordering': ['id'],
            },
        ),
    ]