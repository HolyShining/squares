# Generated by Django 2.2.2 on 2019-06-11 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamehistory',
            name='result',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='cards',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='deck',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='players',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='sequence',
            field=models.CharField(max_length=79, null=True),
        ),
        migrations.AlterField(
            model_name='gamehistory',
            name='squares',
            field=models.IntegerField(null=True),
        ),
    ]
