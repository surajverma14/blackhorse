# Generated by Django 2.2 on 2020-02-23 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=150)),
                ('contact_subject', models.CharField(max_length=150)),
                ('contact_email', models.CharField(max_length=150)),
                ('contact_message', models.TextField()),
            ],
        ),
    ]
