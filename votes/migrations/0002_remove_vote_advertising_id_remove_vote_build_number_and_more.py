# Generated by Django 5.1.7 on 2025-03-11 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='advertising_id',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='build_number',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='email_or_username',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='google_play_services_id',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='iccid',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='imei',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='imsi',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='kernel_version',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='mac_address',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AddField(
            model_name='vote',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
