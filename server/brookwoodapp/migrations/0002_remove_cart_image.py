# Generated by Django 4.1.5 on 2023-05-11 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="image",
        ),
    ]
