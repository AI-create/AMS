# Generated by Django 4.2 on 2024-09-03 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_alter_article_options_alter_tag_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Admin Code',
                'verbose_name_plural': 'Admin Codes',
                'ordering': ['code'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]