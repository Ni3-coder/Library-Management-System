# Generated by Django 3.2.8 on 2022-02-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
