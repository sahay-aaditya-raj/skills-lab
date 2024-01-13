# Generated by Django 5.0.1 on 2024-01-10 09:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(blank=True, max_length=255)),
                ('choice_a', models.CharField(max_length=20)),
                ('choice_b', models.CharField(max_length=20)),
                ('choice_c', models.CharField(max_length=20)),
                ('choice_d', models.CharField(max_length=20)),
                ('correct', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.BooleanField(default=False)),
                ('q2', models.BooleanField(default=False)),
                ('q3', models.BooleanField(default=False)),
                ('q4', models.BooleanField(default=False)),
                ('q5', models.BooleanField(default=False)),
                ('total_score', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
