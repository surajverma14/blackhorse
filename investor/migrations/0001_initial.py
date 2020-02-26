# Generated by Django 2.2.7 on 2019-11-10 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorThesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=150)),
                ('ticket_size', models.CharField(max_length=150)),
                ('return_expectx', models.CharField(max_length=150)),
                ('return_expectp', models.CharField(max_length=150)),
                ('exit_time', models.CharField(max_length=150)),
                ('investor_industry', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InvestorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_entity_name', models.CharField(max_length=150)),
                ('investor_logo', models.ImageField(default='HRS.PNG', upload_to='investor_uploads_logo')),
                ('investor_contact_number', models.CharField(max_length=10)),
                ('investor_email', models.EmailField(max_length=254)),
                ('investor_linkedin', models.URLField()),
                ('investor_full_name', models.CharField(max_length=250)),
                ('user', models.OneToOneField(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]