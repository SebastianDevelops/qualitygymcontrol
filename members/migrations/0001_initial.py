# Generated by Django 4.0 on 2022-07-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('mobile_number', models.CharField(max_length=10, unique=True, verbose_name='Mobile Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('medical_history', models.CharField(blank=True, default='None', max_length=300, verbose_name='Medical History')),
                ('admitted_on', models.DateField(auto_now_add=True)),
                ('registration_date', models.DateField(default='dd/mm/yyyy', verbose_name='Registration Date')),
                ('registration_upto', models.DateField()),
                ('dob', models.DateField(default='dd/mm/yyyy')),
                ('subscription_type', models.CharField(choices=[('gym', 'Gym'), ('cross_fit', 'Cross Fit'), ('gym_and_cross_fit', 'Gym + Cross Fit'), ('pt', 'Personal Training')], default='gym', max_length=30, verbose_name='Subscription Type')),
                ('subscription_period', models.CharField(choices=[('1', '1 Month'), ('2', '2 Months'), ('3', '3 Months'), ('4', '4 Months'), ('5', '5 Months'), ('6', '6 Months'), ('7', '7 Months'), ('8', '8 Months'), ('9', '9 Months'), ('10', '10 Months'), ('11', '11 Months'), ('12', '12 Months')], default='1', max_length=30, verbose_name='Subscription Period')),
                ('amount', models.CharField(max_length=30)),
                ('fee_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending')], default='paid', max_length=30, verbose_name='Fee Status')),
                ('batch', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], default='morning', max_length=30)),
                ('photo', models.FileField(blank=True, upload_to='photos/')),
                ('notification', models.IntegerField(blank=True, default=2)),
                ('stop', models.IntegerField(blank=True, choices=[(0, 'Start'), (1, 'Stop')], default=0, verbose_name='Status')),
            ],
        ),
    ]