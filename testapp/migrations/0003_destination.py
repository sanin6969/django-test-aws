# Generated by Django 5.0.6 on 2024-07-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_user_profile_f_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_username', models.CharField(max_length=50)),
                ('d_password', models.CharField(max_length=50)),
                ('d_foreignkey', models.CharField(max_length=50)),
            ],
        ),
    ]
