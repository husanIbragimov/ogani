# Generated by Django 4.0.6 on 2022-07-08 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=221)),
                ('image', models.ImageField(null=True, upload_to='blog/')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('tag', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
        ),
    ]
