# Generated by Django 3.0.8 on 2020-07-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_assinatura'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='assinatura',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email'),
        ),
    ]
