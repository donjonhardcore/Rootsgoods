# Generated by Django 4.1.7 on 2023-03-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_users_delete_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
