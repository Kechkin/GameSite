# Generated by Django 3.2.7 on 2021-10-01 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='person',
            field=models.ManyToManyField(blank=True, related_name='персонажи', to='base.PersonGame'),
        ),
    ]
