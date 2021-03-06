# Generated by Django 2.2.11 on 2020-04-26 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200313_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='publication',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
