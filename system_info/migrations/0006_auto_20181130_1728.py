# Generated by Django 2.1.3 on 2018-11-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_info', '0005_slave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slave',
            name='ip',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='ip地址'),
        ),
        migrations.AlterField(
            model_name='slave',
            name='name',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='slave别名'),
        ),
    ]