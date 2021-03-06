# Generated by Django 2.2 on 2020-04-16 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20200416_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='a_update_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_crawl_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_create_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='article',
            name='w_update_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_vip_expire_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='vip_order',
            name='v_expire_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.AlterField(
            model_name='vip_order',
            name='v_start_time',
            field=models.IntegerField(default=1587000125),
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_is_origin_num', models.IntegerField(default=0)),
                ('r_put_num', models.IntegerField(default=0)),
                ('r_all_read_num', models.IntegerField(default=0)),
                ('r_origin_avg', models.IntegerField(default=0)),
                ('r_not_origin_avg', models.IntegerField(default=0)),
                ('r_all_watch_num', models.IntegerField(default=0)),
                ('r_all_admire_num', models.IntegerField(default=0)),
                ('r_index', models.IntegerField(default=0)),
                ('r_start_time', models.IntegerField(default=0)),
                ('r_end_time', models.IntegerField(default=0)),
                ('r_update_time', models.IntegerField(default=0)),
                ('r_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Account')),
            ],
            options={
                'db_table': 'wa_rank',
            },
        ),
    ]
