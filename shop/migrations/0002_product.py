# Generated by Django 4.1.3 on 2023-01-13 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ship', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lio', to='shop.cat')),
            ],
        ),
    ]
