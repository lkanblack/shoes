# Generated by Django 2.1.3 on 2020-01-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20200107_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='150x150px', upload_to='img/', verbose_name='Ссылка картинки'),
        ),
    ]