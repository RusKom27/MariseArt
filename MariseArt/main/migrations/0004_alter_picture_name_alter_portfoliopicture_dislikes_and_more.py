# Generated by Django 4.0.3 on 2022-03-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_portfoliopicture_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='name',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliopicture',
            name='dislikes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='portfoliopicture',
            name='likes',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='shoppicture',
            name='price',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='shoppicture',
            name='sells',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
