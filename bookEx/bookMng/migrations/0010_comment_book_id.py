# Generated by Django 4.1 on 2022-11-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookMng", "0009_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment", name="book_id", field=models.IntegerField(null=True),
        ),
    ]