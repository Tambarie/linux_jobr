# Generated by Django 3.1.5 on 2021-02-02 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gbaragboscrumy', '0006_merge_20210202_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scrumygoals',
            options={},
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
