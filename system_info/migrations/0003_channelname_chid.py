# Generated by Django 2.1.3 on 2018-11-27 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_info', '0002_auto_20181126_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='channelname',
            name='chid',
            field=models.CharField(default=None, help_text='频道id', max_length=65, verbose_name='频道id'),
        ),
    ]
