# Generated by Django 3.1.5 on 2021-02-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gbaragboscrumy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_id',
            field=models.IntegerField(),
        ),
    ]
