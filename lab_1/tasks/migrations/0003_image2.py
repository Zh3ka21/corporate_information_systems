# Generated by Django 5.1.1 on 2024-09-13 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
            ],
        ),
    ]
