# Generated by Django 2.1.7 on 2019-04-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarkari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('unit', models.CharField(max_length=150)),
                ('maximum', models.CharField(max_length=150)),
                ('minimum', models.CharField(max_length=150)),
                ('average', models.CharField(max_length=150)),
                ('datee', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'tarkari',
            },
        ),
    ]
