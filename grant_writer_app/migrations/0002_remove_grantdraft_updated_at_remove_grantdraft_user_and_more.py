# Generated by Django 5.1.4 on 2024-12-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grant_writer_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grantdraft',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='grantdraft',
            name='user',
        ),
        migrations.AlterField(
            model_name='grantdraft',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]