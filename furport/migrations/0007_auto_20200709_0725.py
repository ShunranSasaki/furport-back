# Generated by Django 3.0.8 on 2020-07-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("furport", "0006_auto_20200708_1137")]

    operations = [
        migrations.CreateModel(
            name="CharacterTag",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(default="", max_length=255, verbose_name="タグ名"),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="詳細"),
                ),
            ],
            options={"ordering": ("name",)},
        ),
        migrations.CreateModel(
            name="GeneralTag",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(default="", max_length=255, verbose_name="タグ名"),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="詳細"),
                ),
            ],
            options={"ordering": ("name",)},
        ),
        migrations.CreateModel(
            name="OrganizationTag",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(default="", max_length=255, verbose_name="タグ名"),
                ),
                (
                    "description",
                    models.TextField(blank=True, default="", verbose_name="詳細"),
                ),
            ],
            options={"ordering": ("name",)},
        ),
        migrations.RemoveField(model_name="event", name="tag"),
        migrations.DeleteModel(name="Tag"),
        migrations.DeleteModel(name="TagGroup"),
        migrations.AddField(
            model_name="event",
            name="character_tag",
            field=models.ManyToManyField(blank=True, to="furport.CharacterTag"),
        ),
        migrations.AddField(
            model_name="event",
            name="general_tag",
            field=models.ManyToManyField(blank=True, to="furport.GeneralTag"),
        ),
        migrations.AddField(
            model_name="event",
            name="organization_tag",
            field=models.ManyToManyField(blank=True, to="furport.OrganizationTag"),
        ),
    ]
