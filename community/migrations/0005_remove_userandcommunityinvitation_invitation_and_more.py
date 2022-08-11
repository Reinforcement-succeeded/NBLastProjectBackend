# Generated by Django 4.0.6 on 2022-08-10 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_userandcommunityinvitation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userandcommunityinvitation',
            name='invitation',
        ),
        migrations.AddField(
            model_name='userandcommunityinvitation',
            name='request',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userandcommunityinvitation',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userandcommunityinvitation',
            name='invited',
            field=models.BooleanField(default=False),
        ),
    ]
