# Generated by Django 5.0.4 on 2024-04-09 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('current_address', models.CharField(blank=True, max_length=255)),
                ('nationality', models.CharField(blank=True, max_length=50)),
                ('job_title', models.CharField(blank=True, max_length=255)),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('employment_status', models.CharField(blank=True, max_length=50)),
                ('monthly_income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('account_number', models.CharField(blank=True, max_length=20)),
                ('ifsc_code', models.CharField(blank=True, max_length=11)),
                ('bank_name', models.CharField(blank=True, max_length=255)),
                ('upi_id', models.CharField(blank=True, max_length=255)),
                ('pan_card', models.CharField(blank=True, max_length=10)),
                ('aadhaar_card', models.CharField(blank=True, max_length=12)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
