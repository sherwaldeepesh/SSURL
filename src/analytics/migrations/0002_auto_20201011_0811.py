# Generated by Django 2.2.3 on 2020-10-11 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickevent',
            name='ssurl_URL',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='shortner.ssurlURL'),
        ),
    ]