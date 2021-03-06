# Generated by Django 4.0.3 on 2022-03-11 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='default_image.png', null=True, upload_to='')),
                ('name', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='portfoliopicture',
            name='art_picture',
        ),
        migrations.RemoveField(
            model_name='shoppicture',
            name='art_picture',
        ),
        migrations.DeleteModel(
            name='ArtPicture',
        ),
        migrations.AddField(
            model_name='portfoliopicture',
            name='picture',
            field=models.ManyToManyField(blank=True, to='main.picture'),
        ),
        migrations.AddField(
            model_name='shoppicture',
            name='picture',
            field=models.ManyToManyField(blank=True, to='main.picture'),
        ),
    ]
