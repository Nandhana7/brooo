# Generated by Django 4.1.5 on 2023-05-14 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0006_review_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="p_name",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]