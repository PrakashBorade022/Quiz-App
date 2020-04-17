# Generated by Django 2.2 on 2020-04-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qno', models.IntegerField(max_length=4, unique=True)),
                ('question', models.CharField(max_length=300)),
                ('option1', models.CharField(max_length=200)),
                ('option2', models.CharField(max_length=200)),
                ('option3', models.CharField(max_length=200)),
                ('option4', models.CharField(max_length=200)),
                ('ans1', models.CharField(max_length=20)),
                ('ans2', models.CharField(max_length=20)),
                ('ans3', models.CharField(max_length=20)),
                ('ans4', models.CharField(max_length=20)),
            ],
        ),
    ]