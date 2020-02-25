# Generated by Django 3.0.2 on 2020-02-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('mle', models.CharField(max_length=15)),
                ('grade', models.CharField(choices=[('2°CL', '2°classe'), ('1°CL', '2°classe'), ('CAL', 'Caporal'), ('C/C', 'Caporal chef'), ('SGT', 'Sergent'), ('S/C', 'Sergent chef'), ('ADJT', 'Adjudant'), ('A/C', 'Adjudant chef'), ('LT', 'Lieutenant'), ('SLT', 'Sous lieutenant'), ('CNE', 'Capitaine'), ('CDT', 'Commandant'), ('LTCOL', 'Lieutenant Colonel'), ('COL', 'Colonel plein'), ('COLM', 'Colonel Major'), ('GND', 'Général de  brigade')], max_length=5)),
                ('tel', models.IntegerField(max_length=10)),
            ],
        ),
    ]
