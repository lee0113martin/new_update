# Generated by Django 4.2.2 on 2023-06-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni', '0005_alter_items_ids'),
    ]

    operations = [
        migrations.CreateModel(
            name='kana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_Name', models.CharField(max_length=255)),
                ('Brand', models.CharField(max_length=255)),
                ('Quantity', models.IntegerField()),
                ('Condition', models.TextField()),
            ],
        ),
    ]
