# Generated by Django 2.2.dev20180806210306 on 2018-08-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_moodle', models.IntegerField(unique=True)),
                ('codigo_suap', models.IntegerField(unique=True)),
                ('nome_campus', models.CharField(max_length=100)),
            ],
        ),
    ]