# Generated by Django 4.2.5 on 2023-10-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_activities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('restaurant_name', models.TextField()),
                ('restaurant_desc', models.TextField()),
                ('restaurant_signature', models.TextField()),
                ('restaurant_rating', models.IntegerField()),
            ],
        ),
    ]