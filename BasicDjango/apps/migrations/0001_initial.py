# Generated by Django 5.0.6 on 2024-06-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
                ('title', models.CharField(max_length=100)),
                ('pricce', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
