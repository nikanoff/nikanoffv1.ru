# Generated by Django 5.0.4 on 2024-05-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nika', '0007_delete_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]