# Generated by Django 2.2 on 2020-04-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200416_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='a_update_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_crawl_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_create_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_update_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_vip_expire_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vip_order',
            name='v_expire_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vip_order',
            name='v_start_time',
            field=models.IntegerField(default=0),
        ),
    ]