# Generated by Django 4.2.13 on 2024-05-23 11:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("learning_logs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="creation",
            options={"verbose_name_plural": "Creations"},
        ),
        migrations.AlterModelOptions(
            name="shadow",
            options={"verbose_name_plural": "Shadows"},
        ),
    ]
