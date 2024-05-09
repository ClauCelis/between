# Generated by Django 4.2.13 on 2024-05-09 20:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("between_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BigTraditions",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "hemeneutic",
                    models.IntegerField(
                        choices=[
                            (-5, "I feel contrary"),
                            (1, "It sound ok?"),
                            (3, "I feel a little close to it"),
                            (6, "I agree with the premise"),
                            (10, "I feel it is my style"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "phenomenological",
                    models.IntegerField(
                        choices=[
                            (-5, "I feel contrary"),
                            (1, "It sound ok?"),
                            (3, "I feel a little close to it"),
                            (6, "I agree with the premise"),
                            (10, "I feel it is my style"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "cybernetic",
                    models.IntegerField(
                        choices=[
                            (-5, "I feel contrary"),
                            (1, "It sound ok?"),
                            (3, "I feel a little close to it"),
                            (6, "I agree with the premise"),
                            (10, "I feel it is my style"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "spiritual",
                    models.IntegerField(
                        choices=[
                            (-5, "I feel contrary"),
                            (1, "It sound ok?"),
                            (3, "I feel a little close to it"),
                            (6, "I agree with the premise"),
                            (10, "I feel it is my style"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "scientific",
                    models.IntegerField(
                        choices=[
                            (-5, "I feel contrary"),
                            (1, "It sound ok?"),
                            (3, "I feel a little close to it"),
                            (6, "I agree with the premise"),
                            (10, "I feel it is my style"),
                        ],
                        default=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Components",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("body", models.IntegerField(default=0)),
                ("feelings", models.IntegerField(default=0)),
                ("expression", models.IntegerField(default=0)),
                ("thoughts", models.IntegerField(default=0)),
                ("narrative", models.IntegerField(default=0)),
                ("dreaming", models.IntegerField(default=0)),
                ("re_prog", models.IntegerField(default=0)),
                ("subliminal", models.IntegerField(default=0)),
                ("subparts", models.IntegerField(default=0)),
                ("spiritual", models.IntegerField(default=0)),
                ("relational", models.IntegerField(default=0)),
                ("systems", models.IntegerField(default=0)),
                ("setup", models.IntegerField(default=0)),
                ("transOb", models.IntegerField(default=0)),
                ("family", models.IntegerField(default=0)),
                ("antropology", models.IntegerField(default=0)),
                ("arts", models.IntegerField(default=0)),
                ("politics", models.IntegerField(default=0)),
                ("philosophy", models.IntegerField(default=0)),
                ("worldview", models.IntegerField(default=0)),
                ("individuation", models.IntegerField(default=0)),
                ("sex_gender", models.IntegerField(default=0)),
                ("values", models.IntegerField(default=0)),
                ("belonging", models.IntegerField(default=0)),
                ("roles", models.IntegerField(default=0)),
            ],
        ),
    ]
