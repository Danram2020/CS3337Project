# Generated by Django 4.1 on 2022-11-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookMng", "0006_remove_favourite_favourite"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="favourite",
            field=models.BooleanField(default=False),
        ),
    ]
