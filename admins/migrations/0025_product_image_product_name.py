# Generated by Django 4.1.7 on 2023-03-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0024_crops_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]