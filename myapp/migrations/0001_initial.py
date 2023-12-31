# Generated by Django 4.2.2 on 2023-06-25 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(blank=True, upload_to='kitoblar/')),
                ('sarlavha', models.CharField(max_length=255)),
                ('muallif', models.CharField(max_length=255)),
                ('tarif', models.TextField()),
                ('narx', models.IntegerField()),
                ('mavjud_miqdor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=30)),
                ('yetkasiz', models.CharField(max_length=100)),
                ('hudun', models.CharField(max_length=500)),
                ('kitob', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.kitob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
