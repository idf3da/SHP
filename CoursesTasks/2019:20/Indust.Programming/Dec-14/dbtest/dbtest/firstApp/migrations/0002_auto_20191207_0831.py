# Generated by Django 2.2.7 on 2019-12-07 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mistor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ip', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='calchistory',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstApp.Mistor'),
        ),
    ]