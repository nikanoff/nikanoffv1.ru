# Generated by Django 5.0.4 on 2024-05-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nika', '0010_alter_article_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='og_image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
