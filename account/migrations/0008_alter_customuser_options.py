# Generated by Django 4.2.3 on 2023-07-11 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_userbankaccount_is_success'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-date_created']},
        ),
    ]
