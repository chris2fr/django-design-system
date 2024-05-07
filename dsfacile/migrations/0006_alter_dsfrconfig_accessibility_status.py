# Generated by Django 5.0.3 on 2024-04-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsfacile", "0005_dsfacileconfig_notice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dsfacileconfig",
            name="accessibility_status",
            field=models.CharField(
                choices=[("FULL", "fully"), ("PART", "partially"), ("NOT", "not")],
                default="NOT",
                max_length=4,
                verbose_name="Statut de conformité de l’accessibilité",
            ),
        ),
    ]
