# Generated by Django 3.0.8 on 2020-07-17 03:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20200713_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]