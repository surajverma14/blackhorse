# Generated by Django 2.2.7 on 2019-11-15 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0004_auto_20191115_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investorthesis',
            old_name='invesor_ticket_size',
            new_name='investor_ticket_size',
        ),
    ]
