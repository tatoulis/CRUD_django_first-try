# Generated by Django 4.0.2 on 2022-02-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subname', models.CharField(max_length=100)),
                ('object', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'trainer',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
