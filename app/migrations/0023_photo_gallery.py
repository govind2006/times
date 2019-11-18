# Generated by Django 2.2.7 on 2019-11-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_art_culture_book_review_career_education_fashion_health_heritage_science_technology_society'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('link', models.URLField(verbose_name='Link')),
                ('Description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
