# Generated by Django 5.0.4 on 2024-05-15 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nika', '0003_ip_total_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='total_views',
        ),
    ]
