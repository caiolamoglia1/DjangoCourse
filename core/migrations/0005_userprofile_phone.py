# Generated manually on 2025-09-01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(blank=True, max_length=20, verbose_name="Telefone"),
        ),
    ]
