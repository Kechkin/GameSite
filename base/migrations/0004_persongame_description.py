# Generated by Django 3.2.7 on 2021-10-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_persongame_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='persongame',
            name='description',
            field=models.TextField(max_length=250, null=True, verbose_name='Описание'),
        ),
    ]