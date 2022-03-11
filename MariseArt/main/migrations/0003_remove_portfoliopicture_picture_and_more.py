# Generated by Django 4.0.3 on 2022-03-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_picture_remove_portfoliopicture_art_picture_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoliopicture',
            name='picture',
        ),
        migrations.AddField(
            model_name='portfoliopicture',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.picture'),
        ),
        migrations.RemoveField(
            model_name='shoppicture',
            name='picture',
        ),
        migrations.AddField(
            model_name='shoppicture',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.picture'),
        ),
    ]
