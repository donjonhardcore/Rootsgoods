# Generated by Django 4.1.7 on 2023-03-28 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('holdername', models.CharField(default=None, max_length=250, null=True)),
                ('accountnumber', models.CharField(default=None, max_length=250, null=True)),
                ('branch', models.CharField(default=None, max_length=250, null=True)),
                ('ifsc', models.CharField(default=None, max_length=250, null=True)),
                ('bank_name', models.CharField(default=None, max_length=250, null=True)),
                ('user_id', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
