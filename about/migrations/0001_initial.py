# Generated by Django 4.2.19 on 2025-03-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='About My Blog', max_length=200)),
                ('content', models.TextField(help_text='This is the About page content')),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
