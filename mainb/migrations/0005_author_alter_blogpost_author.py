# Generated by Django 4.1.1 on 2022-10-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainb', '0004_alter_blogpost_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Enter your username', max_length=80)),
                ('email', models.EmailField(help_text='Enter your email', max_length=100)),
                ('first_name', models.CharField(help_text='Enter your first name', max_length=100)),
                ('last_name', models.CharField(help_text='Enter your last name', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainb.author'),
        ),
    ]
