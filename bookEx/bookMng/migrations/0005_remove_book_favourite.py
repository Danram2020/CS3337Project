# Generated by Django 4.1 on 2022-11-29 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bookMng", "0004_book_favourite"),
    ]

    operations = [
        migrations.RemoveField(model_name="book", name="favourite",),
    ]
