# Generated by Django 4.1.5 on 2023-05-12 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0002_remove_cart_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="payment",
            old_name="order",
            new_name="orders",
        ),
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ImageField(default=1, upload_to="images"),
            preserve_default=False,
        ),
    ]
