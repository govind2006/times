# Generated by Django 2.2.7 on 2019-11-16 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20191115_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='weeklyspecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('Description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
