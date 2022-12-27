# Generated by Django 4.1.3 on 2022-11-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_writer', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('book_id', models.IntegerField()),
            ],
        ),
    ]
