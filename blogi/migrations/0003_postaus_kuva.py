# Generated by Django 4.1.5 on 2023-03-06 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0002_postaus_luotu'),
    ]

    operations = [
        migrations.AddField(
            model_name='postaus',
            name='kuva',
            field=models.ImageField(null=True, upload_to='blogi/kuvat'),
        ),
    ]
