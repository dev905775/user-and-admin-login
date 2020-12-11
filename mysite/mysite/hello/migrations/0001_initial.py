# Generated by Django 2.2.3 on 2019-08-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=10)),
                ('Lastname', models.CharField(max_length=10)),
                ('Image', models.ImageField(default=0, upload_to='media')),
            ],
        ),
    ]