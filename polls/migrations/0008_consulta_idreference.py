# Generated by Django 4.2.7 on 2023-11-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0007_paciente_idreference"),
    ]

    operations = [
        migrations.AddField(
            model_name="consulta",
            name="IDReference",
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
