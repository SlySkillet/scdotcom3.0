# Generated by Django 5.0.6 on 2024-06-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_api", "0004_tag_blogpost_image_caption_blogpost_tags"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScreenShot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("screenshot", models.ImageField(blank=True, upload_to="images/")),
                ("name", models.CharField(max_length=60)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="TechTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("icon", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("published_date", models.DateTimeField()),
                ("last_updated", models.DateField(auto_now=True)),
                ("title", models.CharField(max_length=200)),
                ("live_link", models.URLField(blank=True, null=True)),
                ("repo_link", models.URLField(blank=True, null=True)),
                (
                    "screenshots",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        related_name="project_images",
                        to="blog_api.screenshot",
                    ),
                ),
                (
                    "primary_tech",
                    models.ManyToManyField(
                        blank=True,
                        related_name="projects_primary",
                        to="blog_api.techtag",
                    ),
                ),
                (
                    "tech_list",
                    models.ManyToManyField(
                        blank=True, related_name="projects", to="blog_api.techtag"
                    ),
                ),
            ],
        ),
    ]
