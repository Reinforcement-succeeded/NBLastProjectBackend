# Generated by Django 4.0.6 on 2022-08-04 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userandcommunityinvitation',
            name='community',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='community.community'),
            preserve_default=False,
        ),
    ]
