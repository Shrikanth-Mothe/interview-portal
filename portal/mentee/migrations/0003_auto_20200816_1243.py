# Generated by Django 3.1 on 2020-08-16 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0002_delete_temptable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='mentee',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentee.mentee'),
        ),
    ]