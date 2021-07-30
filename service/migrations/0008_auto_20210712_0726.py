# Generated by Django 3.2.5 on 2021-07-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_rename_emila_followers_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='followers',
            name='email',
        ),
    ]