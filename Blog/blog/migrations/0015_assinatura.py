# Generated by Django 3.0.8 on 2020-07-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_assunto_eh_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('dt_assinatura', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]