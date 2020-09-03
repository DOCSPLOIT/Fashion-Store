# Generated by Django 3.1 on 2020-08-26 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fashions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashions',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fashions', to=settings.AUTH_USER_MODEL),
        ),
    ]