from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('demand', models.IntegerField()),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text="The ship's name", max_length=10)),
                ('capacity', models.IntegerField(help_text='The capacity of the ship.')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='The name of the terminal', max_length=10)),
                ('capacity', models.IntegerField(help_text='The capacity of the terminal.')),
                ('initial', models.IntegerField(help_text='The initial capacity contained in the terminal')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('ship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.Ship')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.Terminal')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='demand',
            name='terminal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ships.Terminal'),
        ),
    ]
