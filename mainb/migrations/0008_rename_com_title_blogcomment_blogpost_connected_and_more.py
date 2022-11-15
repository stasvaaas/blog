# Generated by Django 4.1.1 on 2022-11-15 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainb', '0007_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='com_title',
            new_name='blogpost_connected',
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, help_text='Enter your first name', max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, help_text='Enter your last name', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]