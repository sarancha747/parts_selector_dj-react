# Generated by Django 3.1.7 on 2021-03-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motherboard',
            name='memory_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parts.memorytype', verbose_name='Memory type'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='primary_gpu_interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parts.gpuinterface', verbose_name='Primary GPU interface'),
        ),
        migrations.AddField(
            model_name='ram',
            name='memory_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parts.memorytype', verbose_name='Memory type'),
        ),
    ]
