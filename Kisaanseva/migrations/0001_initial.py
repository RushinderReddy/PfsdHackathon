# Generated by Django 4.0.2 on 2022-03-17 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.IntegerField()),
                ('name_on_card', models.CharField(max_length=50)),
                ('cardno', models.IntegerField()),
                ('expmonth', models.IntegerField()),
                ('expyear', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
            options={
                'db_table': 'bills',
            },
        ),
        migrations.CreateModel(
            name='book_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('guest', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('date_table', models.DateField(max_length=50)),
                ('time_table', models.TimeField(max_length=60)),
                ('category', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'book_table',
            },
        ),
        migrations.CreateModel(
            name='Contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('query', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Contact_details',
            },
        ),
        migrations.CreateModel(
            name='Feedback_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('mailid', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('cleanliness', models.CharField(max_length=50)),
                ('ResponseTime', models.CharField(max_length=50)),
                ('recommend', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
            options={
                'db_table': 'Feedback_form',
            },
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.URLField(max_length=300)),
            ],
            options={
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordername', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Query_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('dcategory', models.CharField(max_length=50)),
                ('dcapacity', models.CharField(max_length=50)),
                ('dprice', models.CharField(max_length=50)),
                ('dicategory', models.CharField(max_length=50)),
                ('dicapacity', models.CharField(max_length=50)),
                ('diprice', models.CharField(max_length=50)),
                ('tcategory', models.CharField(max_length=50)),
                ('tcapacity', models.CharField(max_length=50)),
                ('tprice', models.CharField(max_length=50)),
                ('pcategory', models.CharField(max_length=50)),
                ('pcapacity', models.CharField(max_length=50)),
                ('pprice', models.CharField(max_length=50)),
                ('rcategory', models.CharField(max_length=50)),
                ('rcapacity', models.CharField(max_length=50)),
                ('rprice', models.CharField(max_length=50)),
                ('decategory', models.CharField(max_length=50)),
                ('decapacity', models.CharField(max_length=50)),
                ('deprice', models.CharField(max_length=50)),
                ('drcategory', models.CharField(max_length=50)),
                ('drcapacity', models.CharField(max_length=50)),
                ('drprice', models.CharField(max_length=50)),
                ('maincategory', models.CharField(max_length=50)),
                ('maincapacity', models.CharField(max_length=50)),
                ('mprice', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Query_table',
            },
        ),
        migrations.CreateModel(
            name='recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('kind', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('newvar', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'recommendations',
            },
        ),
        migrations.CreateModel(
            name='ritem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.URLField(max_length=300)),
            ],
            options={
                'db_table': 'ritem',
            },
        ),
        migrations.CreateModel(
            name='User_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('cpassword', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'User_module',
            },
        ),
        migrations.CreateModel(
            name='storeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('add', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kisaanseva.items')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kisaanseva.user_module')),
            ],
            options={
                'db_table': 'storeItem',
            },
        ),
        migrations.CreateModel(
            name='storefertilizers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('add', models.IntegerField(default=0)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kisaanseva.ritem')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kisaanseva.user_module')),
            ],
            options={
                'db_table': 'storefertilizers',
            },
        ),
        migrations.CreateModel(
            name='orders_food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('cart_items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kisaanseva.storeitem')),
            ],
            options={
                'db_table': 'orders_food',
            },
        ),
    ]
