# Generated by Django 5.0.4 on 2024-04-14 05:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_options_transaction_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PeerToPeer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_peertopeer_transactions', to=settings.AUTH_USER_MODEL, verbose_name='Borrower')),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lent_peertopeer_transactions', to=settings.AUTH_USER_MODEL, verbose_name='Lender')),
            ],
            options={
                'verbose_name_plural': 'Peer To Peers',
            },
        ),
    ]