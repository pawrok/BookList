# Generated by Django 3.2 on 2021-04-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=64)),
                ('author', models.CharField(default='', max_length=64)),
                ('publication_date', models.DateField(default=None)),
                ('ISBN', models.IntegerField(default=0)),
                ('page_count', models.IntegerField(default=0)),
                ('cover_src', models.CharField(default='', max_length=256)),
                ('language', models.IntegerField(default=0)),
            ],
        ),
    ]
