# Generated by Django 5.1.7 on 2025-03-26 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_sitesettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='news_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('biznes', 'Biznes'), ('idman', 'Idman'), ('texnologiya', 'Texnologiya'), ('əyləncə', 'Əyləncə'), ('həyat tərzi', 'Həyat tərzi'), ('qida', 'Qida'), ('elmlər', 'Elmlər'), ('təhsil', 'Təhsil'), ('sağlamlıq', 'Sağlamlıq'), ('korporativ', 'Korporativ'), ('siyasət', 'Siyasət'), ('din', 'Din'), ('cəmiyyət', 'Cəmiyyət')], default='null', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.singlenews')),
            ],
        ),
    ]
