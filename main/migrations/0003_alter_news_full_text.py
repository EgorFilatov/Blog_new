# Generated by Django 4.0.2 on 2022-03-18 11:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_news_annotation_alter_news_full_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст статьи'),
        ),
    ]
