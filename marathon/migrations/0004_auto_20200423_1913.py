# Generated by Django 3.0.5 on 2020-04-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marathon', '0003_auto_20200423_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='charging',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quran',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='selfanalyze',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
