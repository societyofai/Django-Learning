# Generated by Django 3.1.4 on 2021-02-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('studentClass', models.CharField(choices=[('9', '9th'), ('10', '10th'), ('11', '+1'), ('12', '+2')], max_length=255)),
            ],
        ),
    ]
