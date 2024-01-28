# Generated by Django 4.1.7 on 2024-01-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BucketList",
            fields=[
                ("BLid", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.TextField(unique=True)),
                ("isDone", models.BooleanField(default=False)),
                ("DateCreated", models.DateField()),
                ("DateModified", models.DateField()),
            ],
        ),
    ]