# Generated by Django 4.1.7 on 2023-04-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='profile_photo/profile.jpg', upload_to='profile_photo'),
        ),
    ]