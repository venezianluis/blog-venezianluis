# Generated by Django 3.0.8 on 2020-07-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200704_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='assunto',
            field=models.ManyToManyField(to='blog.Assunto'),
        ),
    ]
