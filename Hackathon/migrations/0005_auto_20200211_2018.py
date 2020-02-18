# Generated by Django 3.0.1 on 2020-02-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hackathon', '0004_auto_20200123_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='problem1_selected',
        ),
        migrations.RemoveField(
            model_name='team',
            name='problem2_selected',
        ),
        migrations.RemoveField(
            model_name='team',
            name='problem3_selected',
        ),
        migrations.RemoveField(
            model_name='team',
            name='solution1',
        ),
        migrations.RemoveField(
            model_name='team',
            name='solution2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='solution3',
        ),
        migrations.AddField(
            model_name='team',
            name='domain1',
            field=models.CharField(default='dasf', max_length=30, verbose_name='Domain Preference 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='domain2',
            field=models.CharField(default='default', max_length=30, verbose_name='Domain Preference 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='domain3',
            field=models.CharField(default='default', max_length=30, verbose_name='Domain Preference 3'),
            preserve_default=False,
        ),
    ]