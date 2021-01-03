# Generated by Django 3.0.4 on 2020-12-30 06:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Containt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
                ('title', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
