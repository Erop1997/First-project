# Generated by Django 4.1.7 on 2023-04-04 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_rename_feature_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(default='default description'),
        ),
    ]