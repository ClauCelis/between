# Generated by Django 5.0.6 on 2024-06-11 19:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AfterJournal",
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
                ("question", models.CharField(default=None, max_length=500)),
                ("text", models.TextField(default="")),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Journals",
            },
        ),
        migrations.CreateModel(
            name="Creation",
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
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(default=None, max_length=500)),
                ("goal", models.CharField(default=None, max_length=500)),
                ("text_sensation", models.TextField(default="")),
                ("text_conection", models.TextField(default="")),
                ("text_metaphore", models.TextField(default="")),
                ("text_concepts", models.TextField(default="")),
                ("text_craft", models.TextField(default="")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Creations",
            },
        ),
        migrations.CreateModel(
            name="Shadow",
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
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(default=None, max_length=500)),
                ("goal", models.CharField(default=None, max_length=500)),
                ("text_opossite_style", models.TextField(default="")),
                ("text_opposite_sex", models.TextField(default="")),
                ("text_oppossite_elements", models.TextField(default="")),
                ("text_transf_characters", models.TextField(default="")),
                ("text_furor_curandis", models.TextField(default="")),
                ("text_trauma_history", models.TextField(default="")),
                ("text_trauma_triggers", models.TextField(default="")),
                ("text_care_plan", models.TextField(default="")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Shadows",
            },
        ),
        migrations.CreateModel(
            name="Topic",
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
                ("text", models.CharField(max_length=200)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Entry",
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
                ("text", models.TextField(default="")),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="learning_logs.topic",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "entries",
            },
        ),
    ]
