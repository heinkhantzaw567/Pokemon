# Generated by Django 5.0.1 on 2024-11-24 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctionlisting_element'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='price',
            new_name='starting_bid',
        ),
    ]
