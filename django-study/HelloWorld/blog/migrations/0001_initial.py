# Generated by Django 3.0.6 on 2020-05-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='xixixi', max_length=32)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
