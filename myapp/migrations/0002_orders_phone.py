# Generated by Django 4.2.7 on 2024-11-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=111, max_length=12, verbose_name='Телефон'),
            preserve_default=False,
        ),
    ]
