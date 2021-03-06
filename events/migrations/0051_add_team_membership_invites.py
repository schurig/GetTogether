# Generated by Django 2.0.12 on 2019-08-02 20:51

import datetime
import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("events", "0050_add_attendee_limit")]

    operations = [
        migrations.CreateModel(
            name="TeamMembershipRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("invite_email", models.EmailField(max_length=254)),
                (
                    "request_origin",
                    models.SmallIntegerField(
                        choices=[(0, "Team"), (1, "User")],
                        db_index=True,
                        default=0,
                        verbose_name="Request from",
                    ),
                ),
                ("request_key", models.UUIDField(default=uuid.uuid4)),
                ("requested_date", models.DateTimeField(default=datetime.datetime.now)),
                ("joined_date", models.DateTimeField(blank=True, null=True)),
                (
                    "accepted_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="accepted_team_memberships",
                        to="events.UserProfile",
                    ),
                ),
                (
                    "requested_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="requested_team_memberships",
                        to="events.UserProfile",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="team",
            name="access",
            field=models.SmallIntegerField(
                choices=[(0, "Public"), (1, "Personal"), (2, "Private")],
                default=0,
                verbose_name="Visibility",
            ),
        ),
        migrations.AddField(
            model_name="teammembershiprequest",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="events.Team"
            ),
        ),
        migrations.AddField(
            model_name="teammembershiprequest",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="events.UserProfile",
            ),
        ),
    ]
