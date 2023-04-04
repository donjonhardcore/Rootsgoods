# Generated by Django 4.1.7 on 2023-03-28 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0006_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default=None, max_length=250, null=True)),
                ('name', models.CharField(default=None, max_length=250, null=True)),
                ('email', models.CharField(default=None, max_length=250, null=True)),
                ('password', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
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
        migrations.CreateModel(
            name='Qualityparam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('certificat_id', models.CharField(default=None, max_length=250, null=True)),
                ('location', models.CharField(default=None, max_length=250, null=True)),
                ('image', models.CharField(default=None, max_length=250, null=True)),
                ('cropid', models.CharField(default=None, max_length=250, null=True)),
                ('testid', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactionhistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(default=None, max_length=250, null=True)),
                ('productid', models.CharField(default=None, max_length=250, null=True)),
                ('amount', models.CharField(default=None, max_length=250, null=True)),
                ('datetime', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
        ),
    ]
