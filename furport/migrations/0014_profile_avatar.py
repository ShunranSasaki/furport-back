# Generated by Django 3.0.8 on 2020-07-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("furport", "0013_profile_is_moderator"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="avatar",
            field=models.CharField(
                blank=True, default="", max_length=255, verbose_name="アバター画像URL"
            ),
        ),
    ]