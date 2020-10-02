# Generated by Django 3.0.6 on 2020-09-30 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bj_app', '0002_auto_20200925_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bj_item',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]