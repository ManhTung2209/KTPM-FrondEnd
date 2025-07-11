# Generated by Django 4.2 on 2025-06-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Household",
            fields=[
                ("household_id", models.AutoField(primary_key=True, serialize=False)),
                ("block_name", models.CharField(max_length=50)),
                ("room_number", models.CharField(max_length=10)),
                ("owner_name", models.CharField(max_length=100)),
                ("number_people", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Citizen",
            fields=[
                ("citizen_id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("male", "Nam"), ("female", "Nữ")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "birth_place",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "origin_place",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "id_card_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("id_card_issue_date", models.DateField(blank=True, null=True)),
                (
                    "id_card_issue_place",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("sinh_song", "Sinh sống"),
                            ("tam_vang", "Tạm vắng"),
                            ("tam_tru", "Tạm trú"),
                        ],
                        default="sinh_song",
                        max_length=20,
                    ),
                ),
                (
                    "household",
                    models.ForeignKey(
                        db_column="household_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="HouseHold_Resident.household",
                    ),
                ),
            ],
        ),
    ]
