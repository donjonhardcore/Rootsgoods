# Generated by Django 4.1.7 on 2023-03-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0012_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('roleid', models.CharField(default=None, max_length=250, null=True)),
                ('userid', models.CharField(default=None, max_length=250, null=True)),
                ('productid', models.CharField(default=None, max_length=250, null=True)),
                ('datetime', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
        ),
    ]
