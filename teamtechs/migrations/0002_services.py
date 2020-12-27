# Generated by Django 3.1.3 on 2020-12-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamtechs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
