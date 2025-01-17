# Generated by Django 4.2 on 2024-02-29 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("attachments", "0001_initial"),
        ("calendars", "0002_alter_calendar_admins_alter_calendar_creator_and_more"),
        ("events", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="attachment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="attachment",
                to="attachments.attachment",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="calendar",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="calendar",
                to="calendars.calendar",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="dresscode",
            field=models.CharField(max_length=50),
        ),
    ]
