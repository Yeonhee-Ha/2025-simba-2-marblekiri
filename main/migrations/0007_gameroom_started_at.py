# Generated by Django 5.2.3 on 2025-06-20 23:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_gameroom_current_round_alter_playerinroom_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameroom',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
