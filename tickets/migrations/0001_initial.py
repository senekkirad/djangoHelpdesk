# Generated by Django 4.2.6 on 2023-10-11 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
                ('department', models.IntegerField(choices=[(1, 'IT'), (2, 'Admin'), (3, 'HR'), (4, 'Maintenance')], verbose_name='Department')),
                ('seat_no', models.CharField(max_length=10, verbose_name='Seat No')),
                ('created_on', models.DateTimeField(auto_now=True, verbose_name='Created On')),
                ('status', models.IntegerField(choices=[(3, 'Resolved'), (1, 'Unassigned'), (2, 'Pending')], default=1, verbose_name='Status')),
                ('priority', models.IntegerField(choices=[(1, 'Critical'), (2, 'High'), (3, 'Normal'), (4, 'Low')], verbose_name='Priority')),
                ('created_by', models.EmailField(max_length=254, verbose_name='Created By')),
                ('accepted_by', models.EmailField(max_length=254, null=True, verbose_name='Accepted By')),
            ],
            options={
                'ordering': ('created_on',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=150, verbose_name='Message')),
                ('published_by', models.CharField(default='user', max_length=5, verbose_name='Published By')),
                ('published_at', models.DateTimeField(auto_now=True, verbose_name='Published At')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.ticket')),
            ],
        ),
    ]
