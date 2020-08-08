# Generated by Django 3.0.5 on 2020-05-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_country_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_abr', models.CharField(max_length=3)),
                ('country', models.CharField(max_length=55)),
            ],
        ),
        migrations.RenameModel(
            old_name='country_data',
            new_name='active_countries',
        ),
    ]