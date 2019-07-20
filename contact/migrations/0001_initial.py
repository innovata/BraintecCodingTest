# Generated by Django 2.2.3 on 2019-07-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=64)),
            ],
        ),
    ]