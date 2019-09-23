# Generated by Django 2.2.5 on 2019-09-22 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_auto_20190922_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='sub_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Quiz.SubCategory', verbose_name='Sub-Category'),
        ),
    ]