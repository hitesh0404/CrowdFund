# Generated by Django 5.1.4 on 2024-12-13 07:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='motive',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('281a5307-163d-4e33-b4c7-941f862bcd5b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='motive',
            name='logo',
            field=models.ImageField(upload_to='image/motive/logo/'),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.UUID('d4387ca2-fc2e-4821-9b10-f447786adb33'), primary_key=True, serialize=False)),
                ('dp', models.ImageField(upload_to='image/group/dp/')),
                ('name', models.CharField(default=models.UUIDField(auto_created=True, default=uuid.UUID('d4387ca2-fc2e-4821-9b10-f447786adb33'), primary_key=True, serialize=False), max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('motive', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='community.motive')),
            ],
        ),
        migrations.CreateModel(
            name='GroupContributor',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.UUID('6275f37b-f973-4ca2-905e-08564359f8c4'), primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Creator', 'Creator'), ('User', 'User')], default='User', max_length=50)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='community.group')),
            ],
            options={
                'unique_together': {('contributor', 'group')},
            },
        ),
        migrations.CreateModel(
            name='InitiatorGroupContributor',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.UUID('fb19cff4-14c5-4fa2-8a7e-9543f445e174'), primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Creator', 'Creator'), ('User', 'User')], default='User', max_length=50)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='community.group')),
            ],
            options={
                'unique_together': {('contributor', 'group')},
            },
        ),
    ]
