# Generated by Django 4.2.3 on 2023-08-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisment', '0004_advertisment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='advertisment/', verbose_name='Изображение'),
        ),
    ]
