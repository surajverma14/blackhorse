# Generated by Django 2.2.7 on 2019-11-19 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0005_auto_20191115_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorthesis',
            name='investor_business_model',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
