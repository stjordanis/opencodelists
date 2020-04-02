# Generated by Django 2.2.11 on 2020-04-02 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('coding_system', models.CharField(choices=[('readv2', 'Read V2'), ('ctv3', 'Clinical Terms Version 3 (Read V3)'), ('snomedct', 'SNOMED CT')], max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CodelistVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=12)),
                ('codelist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='codelists.Codelist')),
            ],
            options={
                'unique_together': {('codelist', 'version')},
            },
        ),
        migrations.AddField(
            model_name='codelist',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codelists', to='codelists.Publisher'),
        ),
        migrations.CreateModel(
            name='CodelistMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=18)),
                ('codelist_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='codelists.CodelistVersion')),
            ],
            options={
                'unique_together': {('codelist_version', 'value')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='codelist',
            unique_together={('publisher', 'slug')},
        ),
    ]
