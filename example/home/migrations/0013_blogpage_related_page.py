# Generated by Django 2.2.1 on 2019-10-02 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("home", "0012_auto_20191002_1154"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="related_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.Page",
            ),
        )
    ]