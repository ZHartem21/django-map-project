# Generated by Django 4.2 on 2023-04-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_alter_image_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to=''),
        ),
    ]
