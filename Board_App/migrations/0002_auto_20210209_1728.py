# Generated by Django 3.1.6 on 2021-02-09 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Board_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]
