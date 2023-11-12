# Generated by Django 4.2.5 on 2023-10-25 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0004_rename_projectimages_project_projectimage_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogCategory",
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
                ("name", models.CharField(max_length=500)),
                ("blogResume", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="BlogFile",
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
                ("file", models.CharField(max_length=255)),
                ("fileContent", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_files",
                        to="tasks.blogcategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SkillsImages",
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
                (
                    "programingLanguageImages",
                    models.ImageField(
                        blank=True, upload_to="programming_language_images/"
                    ),
                ),
                (
                    "userInterfaceImages",
                    models.ImageField(blank=True, upload_to="user_interface_images/"),
                ),
                (
                    "developmentToolsImages",
                    models.ImageField(
                        blank=True, upload_to="development_tools_images/"
                    ),
                ),
                (
                    "databasesImages",
                    models.ImageField(blank=True, upload_to="databases_images/"),
                ),
                (
                    "dataProcessingImages",
                    models.ImageField(blank=True, upload_to="data_processing_images/"),
                ),
                (
                    "operatingSystemsImages",
                    models.ImageField(
                        blank=True, upload_to="operating_systems_images/"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Blog",
        ),
        migrations.RenameField(
            model_name="projectimages",
            old_name="Project",
            new_name="project",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="dataProcessingImages",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="databasesImages",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="developmentToolsImages",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="operatingSystemsImages",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="programingLanguageImages",
        ),
        migrations.RemoveField(
            model_name="skill",
            name="userInterfaceImages",
        ),
        migrations.AlterField(
            model_name="project",
            name="projectComplete",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="projectResume",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="projectimages",
            name="projectWebsiteImages",
            field=models.ImageField(blank=True, upload_to="project_website_images/"),
        ),
        migrations.AlterField(
            model_name="projectimages",
            name="projectWebsiteTools",
            field=models.ImageField(
                blank=True, upload_to="project_website_images_tools/"
            ),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skillComplete",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="skill",
            name="skillsResume",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="skillsimages",
            name="skills",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tasks.skill"
            ),
        ),
    ]
