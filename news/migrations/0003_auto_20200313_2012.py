# Generated by Django 2.2.11 on 2020-03-13 14:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_auto_20200313_2011'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Publication',
        ),
    ]
