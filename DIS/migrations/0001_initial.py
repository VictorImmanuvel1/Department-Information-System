# Generated by Django 2.1.7 on 2021-04-14 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.CharField(blank=True, max_length=200, null=True)),
                ('s1', models.CharField(blank=True, max_length=200, null=True)),
                ('c1', models.CharField(blank=True, max_length=200, null=True)),
                ('y1', models.CharField(blank=True, max_length=200, null=True)),
                ('d2', models.CharField(blank=True, max_length=200, null=True)),
                ('s2', models.CharField(blank=True, max_length=200, null=True)),
                ('c2', models.CharField(blank=True, max_length=200, null=True)),
                ('y2', models.CharField(blank=True, max_length=200, null=True)),
                ('d3', models.CharField(blank=True, max_length=200, null=True)),
                ('s3', models.CharField(blank=True, max_length=200, null=True)),
                ('c3', models.CharField(blank=True, max_length=200, null=True)),
                ('y3', models.CharField(blank=True, max_length=200, null=True)),
                ('d4', models.CharField(blank=True, max_length=200, null=True)),
                ('s4', models.CharField(blank=True, max_length=200, null=True)),
                ('c4', models.CharField(blank=True, max_length=200, null=True)),
                ('y4', models.CharField(blank=True, max_length=200, null=True)),
                ('d5', models.CharField(blank=True, max_length=200, null=True)),
                ('s5', models.CharField(blank=True, max_length=200, null=True)),
                ('c5', models.CharField(blank=True, max_length=200, null=True)),
                ('y5', models.CharField(blank=True, max_length=200, null=True)),
                ('d6', models.CharField(blank=True, max_length=200, null=True)),
                ('s6', models.CharField(blank=True, max_length=200, null=True)),
                ('c6', models.CharField(blank=True, max_length=200, null=True)),
                ('y6', models.CharField(blank=True, max_length=200, null=True)),
                ('d7', models.CharField(blank=True, max_length=200, null=True)),
                ('s7', models.CharField(blank=True, max_length=200, null=True)),
                ('c7', models.CharField(blank=True, max_length=200, null=True)),
                ('y7', models.CharField(blank=True, max_length=200, null=True)),
                ('d8', models.CharField(blank=True, max_length=200, null=True)),
                ('s8', models.CharField(blank=True, max_length=200, null=True)),
                ('c8', models.CharField(blank=True, max_length=200, null=True)),
                ('y8', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('department', models.CharField(blank=True, max_length=200, null=True)),
                ('doj', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('spint', models.TextField(blank=True, null=True)),
                ('spinre', models.CharField(blank=True, max_length=200, null=True)),
                ('reint', models.CharField(blank=True, max_length=200, null=True)),
                ('oe', models.TextField(blank=True, null=True)),
                ('ae', models.TextField(blank=True, null=True)),
                ('app', models.TextField(blank=True, null=True)),
                ('csw', models.TextField(blank=True, null=True)),
                ('oa', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='sem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC1', models.CharField(default='--', max_length=100)),
                ('SN1', models.CharField(default='--', max_length=100)),
                ('T11', models.CharField(default='--', max_length=100)),
                ('Q11', models.CharField(default='--', max_length=100)),
                ('A11', models.CharField(default='--', max_length=100)),
                ('T21', models.CharField(default='--', max_length=100)),
                ('Q21', models.CharField(default='--', max_length=100)),
                ('A21', models.CharField(default='--', max_length=100)),
                ('TO1', models.CharField(default='--', max_length=100)),
                ('E1', models.CharField(default='--', max_length=100)),
                ('SC2', models.CharField(default='--', max_length=100)),
                ('SN2', models.CharField(default='--', max_length=100)),
                ('T12', models.CharField(default='--', max_length=100)),
                ('Q12', models.CharField(default='--', max_length=100)),
                ('A12', models.CharField(default='--', max_length=100)),
                ('T22', models.CharField(default='--', max_length=100)),
                ('Q22', models.CharField(default='--', max_length=100)),
                ('A22', models.CharField(default='--', max_length=100)),
                ('TO2', models.CharField(default='--', max_length=100)),
                ('E2', models.CharField(default='--', max_length=100)),
                ('SC3', models.CharField(default='--', max_length=100)),
                ('SN3', models.CharField(default='--', max_length=100)),
                ('T13', models.CharField(default='--', max_length=100)),
                ('Q13', models.CharField(default='--', max_length=100)),
                ('A13', models.CharField(default='--', max_length=100)),
                ('T23', models.CharField(default='--', max_length=100)),
                ('Q23', models.CharField(default='--', max_length=100)),
                ('A23', models.CharField(default='--', max_length=100)),
                ('TO3', models.CharField(default='--', max_length=100)),
                ('E3', models.CharField(default='--', max_length=100)),
                ('SC4', models.CharField(default='--', max_length=100)),
                ('SN4', models.CharField(default='--', max_length=100)),
                ('T14', models.CharField(default='--', max_length=100)),
                ('Q14', models.CharField(default='--', max_length=100)),
                ('A14', models.CharField(default='--', max_length=100)),
                ('T24', models.CharField(default='--', max_length=100)),
                ('Q24', models.CharField(default='--', max_length=100)),
                ('A24', models.CharField(default='--', max_length=100)),
                ('TO4', models.CharField(default='--', max_length=100)),
                ('E4', models.CharField(default='--', max_length=100)),
                ('SC5', models.CharField(default='--', max_length=100)),
                ('SN5', models.CharField(default='--', max_length=100)),
                ('T15', models.CharField(default='--', max_length=100)),
                ('Q15', models.CharField(default='--', max_length=100)),
                ('A15', models.CharField(default='--', max_length=100)),
                ('T25', models.CharField(default='--', max_length=100)),
                ('Q25', models.CharField(default='--', max_length=100)),
                ('A25', models.CharField(default='--', max_length=100)),
                ('TO5', models.CharField(default='--', max_length=100)),
                ('E5', models.CharField(default='--', max_length=100)),
                ('SC6', models.CharField(default='--', max_length=100)),
                ('SN6', models.CharField(default='--', max_length=100)),
                ('T16', models.CharField(default='--', max_length=100)),
                ('Q16', models.CharField(default='--', max_length=100)),
                ('A16', models.CharField(default='--', max_length=100)),
                ('T26', models.CharField(default='--', max_length=100)),
                ('Q26', models.CharField(default='--', max_length=100)),
                ('A26', models.CharField(default='--', max_length=100)),
                ('TO6', models.CharField(default='--', max_length=100)),
                ('E6', models.CharField(default='--', max_length=100)),
                ('SC7', models.CharField(default='--', max_length=100)),
                ('SN7', models.CharField(default='--', max_length=100)),
                ('T17', models.CharField(default='--', max_length=100)),
                ('Q17', models.CharField(default='--', max_length=100)),
                ('A17', models.CharField(default='--', max_length=100)),
                ('T27', models.CharField(default='--', max_length=100)),
                ('Q27', models.CharField(default='--', max_length=100)),
                ('A27', models.CharField(default='--', max_length=100)),
                ('TO7', models.CharField(default='--', max_length=100)),
                ('E7', models.CharField(default='--', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sem2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC1', models.CharField(default='--', max_length=100)),
                ('SN1', models.CharField(default='--', max_length=100)),
                ('T11', models.CharField(default='--', max_length=100)),
                ('Q11', models.CharField(default='--', max_length=100)),
                ('A11', models.CharField(default='--', max_length=100)),
                ('T21', models.CharField(default='--', max_length=100)),
                ('Q21', models.CharField(default='--', max_length=100)),
                ('A21', models.CharField(default='--', max_length=100)),
                ('TO1', models.CharField(default='--', max_length=100)),
                ('E1', models.CharField(default='--', max_length=100)),
                ('SC2', models.CharField(default='--', max_length=100)),
                ('SN2', models.CharField(default='--', max_length=100)),
                ('T12', models.CharField(default='--', max_length=100)),
                ('Q12', models.CharField(default='--', max_length=100)),
                ('A12', models.CharField(default='--', max_length=100)),
                ('T22', models.CharField(default='--', max_length=100)),
                ('Q22', models.CharField(default='--', max_length=100)),
                ('A22', models.CharField(default='--', max_length=100)),
                ('TO2', models.CharField(default='--', max_length=100)),
                ('E2', models.CharField(default='--', max_length=100)),
                ('SC3', models.CharField(default='--', max_length=100)),
                ('SN3', models.CharField(default='--', max_length=100)),
                ('T13', models.CharField(default='--', max_length=100)),
                ('Q13', models.CharField(default='--', max_length=100)),
                ('A13', models.CharField(default='--', max_length=100)),
                ('T23', models.CharField(default='--', max_length=100)),
                ('Q23', models.CharField(default='--', max_length=100)),
                ('A23', models.CharField(default='--', max_length=100)),
                ('TO3', models.CharField(default='--', max_length=100)),
                ('E3', models.CharField(default='--', max_length=100)),
                ('SC4', models.CharField(default='--', max_length=100)),
                ('SN4', models.CharField(default='--', max_length=100)),
                ('T14', models.CharField(default='--', max_length=100)),
                ('Q14', models.CharField(default='--', max_length=100)),
                ('A14', models.CharField(default='--', max_length=100)),
                ('T24', models.CharField(default='--', max_length=100)),
                ('Q24', models.CharField(default='--', max_length=100)),
                ('A24', models.CharField(default='--', max_length=100)),
                ('TO4', models.CharField(default='--', max_length=100)),
                ('E4', models.CharField(default='--', max_length=100)),
                ('SC5', models.CharField(default='--', max_length=100)),
                ('SN5', models.CharField(default='--', max_length=100)),
                ('T15', models.CharField(default='--', max_length=100)),
                ('Q15', models.CharField(default='--', max_length=100)),
                ('A15', models.CharField(default='--', max_length=100)),
                ('T25', models.CharField(default='--', max_length=100)),
                ('Q25', models.CharField(default='--', max_length=100)),
                ('A25', models.CharField(default='--', max_length=100)),
                ('TO5', models.CharField(default='--', max_length=100)),
                ('E5', models.CharField(default='--', max_length=100)),
                ('SC6', models.CharField(default='--', max_length=100)),
                ('SN6', models.CharField(default='--', max_length=100)),
                ('T16', models.CharField(default='--', max_length=100)),
                ('Q16', models.CharField(default='--', max_length=100)),
                ('A16', models.CharField(default='--', max_length=100)),
                ('T26', models.CharField(default='--', max_length=100)),
                ('Q26', models.CharField(default='--', max_length=100)),
                ('A26', models.CharField(default='--', max_length=100)),
                ('TO6', models.CharField(default='--', max_length=100)),
                ('E6', models.CharField(default='--', max_length=100)),
                ('SC7', models.CharField(default='--', max_length=100)),
                ('SN7', models.CharField(default='--', max_length=100)),
                ('T17', models.CharField(default='--', max_length=100)),
                ('Q17', models.CharField(default='--', max_length=100)),
                ('A17', models.CharField(default='--', max_length=100)),
                ('T27', models.CharField(default='--', max_length=100)),
                ('Q27', models.CharField(default='--', max_length=100)),
                ('A27', models.CharField(default='--', max_length=100)),
                ('TO7', models.CharField(default='--', max_length=100)),
                ('E7', models.CharField(default='--', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sem3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC1', models.CharField(default='--', max_length=100)),
                ('SN1', models.CharField(default='--', max_length=100)),
                ('T11', models.CharField(default='--', max_length=100)),
                ('Q11', models.CharField(default='--', max_length=100)),
                ('A11', models.CharField(default='--', max_length=100)),
                ('T21', models.CharField(default='--', max_length=100)),
                ('Q21', models.CharField(default='--', max_length=100)),
                ('A21', models.CharField(default='--', max_length=100)),
                ('TO1', models.CharField(default='--', max_length=100)),
                ('E1', models.CharField(default='--', max_length=100)),
                ('SC2', models.CharField(default='--', max_length=100)),
                ('SN2', models.CharField(default='--', max_length=100)),
                ('T12', models.CharField(default='--', max_length=100)),
                ('Q12', models.CharField(default='--', max_length=100)),
                ('A12', models.CharField(default='--', max_length=100)),
                ('T22', models.CharField(default='--', max_length=100)),
                ('Q22', models.CharField(default='--', max_length=100)),
                ('A22', models.CharField(default='--', max_length=100)),
                ('TO2', models.CharField(default='--', max_length=100)),
                ('E2', models.CharField(default='--', max_length=100)),
                ('SC3', models.CharField(default='--', max_length=100)),
                ('SN3', models.CharField(default='--', max_length=100)),
                ('T13', models.CharField(default='--', max_length=100)),
                ('Q13', models.CharField(default='--', max_length=100)),
                ('A13', models.CharField(default='--', max_length=100)),
                ('T23', models.CharField(default='--', max_length=100)),
                ('Q23', models.CharField(default='--', max_length=100)),
                ('A23', models.CharField(default='--', max_length=100)),
                ('TO3', models.CharField(default='--', max_length=100)),
                ('E3', models.CharField(default='--', max_length=100)),
                ('SC4', models.CharField(default='--', max_length=100)),
                ('SN4', models.CharField(default='--', max_length=100)),
                ('T14', models.CharField(default='--', max_length=100)),
                ('Q14', models.CharField(default='--', max_length=100)),
                ('A14', models.CharField(default='--', max_length=100)),
                ('T24', models.CharField(default='--', max_length=100)),
                ('Q24', models.CharField(default='--', max_length=100)),
                ('A24', models.CharField(default='--', max_length=100)),
                ('TO4', models.CharField(default='--', max_length=100)),
                ('E4', models.CharField(default='--', max_length=100)),
                ('SC5', models.CharField(default='--', max_length=100)),
                ('SN5', models.CharField(default='--', max_length=100)),
                ('T15', models.CharField(default='--', max_length=100)),
                ('Q15', models.CharField(default='--', max_length=100)),
                ('A15', models.CharField(default='--', max_length=100)),
                ('T25', models.CharField(default='--', max_length=100)),
                ('Q25', models.CharField(default='--', max_length=100)),
                ('A25', models.CharField(default='--', max_length=100)),
                ('TO5', models.CharField(default='--', max_length=100)),
                ('E5', models.CharField(default='--', max_length=100)),
                ('SC6', models.CharField(default='--', max_length=100)),
                ('SN6', models.CharField(default='--', max_length=100)),
                ('T16', models.CharField(default='--', max_length=100)),
                ('Q16', models.CharField(default='--', max_length=100)),
                ('A16', models.CharField(default='--', max_length=100)),
                ('T26', models.CharField(default='--', max_length=100)),
                ('Q26', models.CharField(default='--', max_length=100)),
                ('A26', models.CharField(default='--', max_length=100)),
                ('TO6', models.CharField(default='--', max_length=100)),
                ('E6', models.CharField(default='--', max_length=100)),
                ('SC7', models.CharField(default='--', max_length=100)),
                ('SN7', models.CharField(default='--', max_length=100)),
                ('T17', models.CharField(default='--', max_length=100)),
                ('Q17', models.CharField(default='--', max_length=100)),
                ('A17', models.CharField(default='--', max_length=100)),
                ('T27', models.CharField(default='--', max_length=100)),
                ('Q27', models.CharField(default='--', max_length=100)),
                ('A27', models.CharField(default='--', max_length=100)),
                ('TO7', models.CharField(default='--', max_length=100)),
                ('E7', models.CharField(default='--', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sem4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC1', models.CharField(default='--', max_length=100)),
                ('SN1', models.CharField(default='--', max_length=100)),
                ('T11', models.CharField(default='--', max_length=100)),
                ('Q11', models.CharField(default='--', max_length=100)),
                ('A11', models.CharField(default='--', max_length=100)),
                ('T21', models.CharField(default='--', max_length=100)),
                ('Q21', models.CharField(default='--', max_length=100)),
                ('A21', models.CharField(default='--', max_length=100)),
                ('TO1', models.CharField(default='--', max_length=100)),
                ('E1', models.CharField(default='--', max_length=100)),
                ('SC2', models.CharField(default='--', max_length=100)),
                ('SN2', models.CharField(default='--', max_length=100)),
                ('T12', models.CharField(default='--', max_length=100)),
                ('Q12', models.CharField(default='--', max_length=100)),
                ('A12', models.CharField(default='--', max_length=100)),
                ('T22', models.CharField(default='--', max_length=100)),
                ('Q22', models.CharField(default='--', max_length=100)),
                ('A22', models.CharField(default='--', max_length=100)),
                ('TO2', models.CharField(default='--', max_length=100)),
                ('E2', models.CharField(default='--', max_length=100)),
                ('SC3', models.CharField(default='--', max_length=100)),
                ('SN3', models.CharField(default='--', max_length=100)),
                ('T13', models.CharField(default='--', max_length=100)),
                ('Q13', models.CharField(default='--', max_length=100)),
                ('A13', models.CharField(default='--', max_length=100)),
                ('T23', models.CharField(default='--', max_length=100)),
                ('Q23', models.CharField(default='--', max_length=100)),
                ('A23', models.CharField(default='--', max_length=100)),
                ('TO3', models.CharField(default='--', max_length=100)),
                ('E3', models.CharField(default='--', max_length=100)),
                ('SC4', models.CharField(default='--', max_length=100)),
                ('SN4', models.CharField(default='--', max_length=100)),
                ('T14', models.CharField(default='--', max_length=100)),
                ('Q14', models.CharField(default='--', max_length=100)),
                ('A14', models.CharField(default='--', max_length=100)),
                ('T24', models.CharField(default='--', max_length=100)),
                ('Q24', models.CharField(default='--', max_length=100)),
                ('A24', models.CharField(default='--', max_length=100)),
                ('TO4', models.CharField(default='--', max_length=100)),
                ('E4', models.CharField(default='--', max_length=100)),
                ('SC5', models.CharField(default='--', max_length=100)),
                ('SN5', models.CharField(default='--', max_length=100)),
                ('T15', models.CharField(default='--', max_length=100)),
                ('Q15', models.CharField(default='--', max_length=100)),
                ('A15', models.CharField(default='--', max_length=100)),
                ('T25', models.CharField(default='--', max_length=100)),
                ('Q25', models.CharField(default='--', max_length=100)),
                ('A25', models.CharField(default='--', max_length=100)),
                ('TO5', models.CharField(default='--', max_length=100)),
                ('E5', models.CharField(default='--', max_length=100)),
                ('SC6', models.CharField(default='--', max_length=100)),
                ('SN6', models.CharField(default='--', max_length=100)),
                ('T16', models.CharField(default='--', max_length=100)),
                ('Q16', models.CharField(default='--', max_length=100)),
                ('A16', models.CharField(default='--', max_length=100)),
                ('T26', models.CharField(default='--', max_length=100)),
                ('Q26', models.CharField(default='--', max_length=100)),
                ('A26', models.CharField(default='--', max_length=100)),
                ('TO6', models.CharField(default='--', max_length=100)),
                ('E6', models.CharField(default='--', max_length=100)),
                ('SC7', models.CharField(default='--', max_length=100)),
                ('SN7', models.CharField(default='--', max_length=100)),
                ('T17', models.CharField(default='--', max_length=100)),
                ('Q17', models.CharField(default='--', max_length=100)),
                ('A17', models.CharField(default='--', max_length=100)),
                ('T27', models.CharField(default='--', max_length=100)),
                ('Q27', models.CharField(default='--', max_length=100)),
                ('A27', models.CharField(default='--', max_length=100)),
                ('TO7', models.CharField(default='--', max_length=100)),
                ('E7', models.CharField(default='--', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='sem5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SC1', models.CharField(default='--', max_length=100)),
                ('SN1', models.CharField(default='--', max_length=100)),
                ('T11', models.CharField(default='--', max_length=100)),
                ('Q11', models.CharField(default='--', max_length=100)),
                ('A11', models.CharField(default='--', max_length=100)),
                ('T21', models.CharField(default='--', max_length=100)),
                ('Q21', models.CharField(default='--', max_length=100)),
                ('A21', models.CharField(default='--', max_length=100)),
                ('TO1', models.CharField(default='--', max_length=100)),
                ('E1', models.CharField(default='--', max_length=100)),
                ('SC2', models.CharField(default='--', max_length=100)),
                ('SN2', models.CharField(default='--', max_length=100)),
                ('T12', models.CharField(default='--', max_length=100)),
                ('Q12', models.CharField(default='--', max_length=100)),
                ('A12', models.CharField(default='--', max_length=100)),
                ('T22', models.CharField(default='--', max_length=100)),
                ('Q22', models.CharField(default='--', max_length=100)),
                ('A22', models.CharField(default='--', max_length=100)),
                ('TO2', models.CharField(default='--', max_length=100)),
                ('E2', models.CharField(default='--', max_length=100)),
                ('SC3', models.CharField(default='--', max_length=100)),
                ('SN3', models.CharField(default='--', max_length=100)),
                ('T13', models.CharField(default='--', max_length=100)),
                ('Q13', models.CharField(default='--', max_length=100)),
                ('A13', models.CharField(default='--', max_length=100)),
                ('T23', models.CharField(default='--', max_length=100)),
                ('Q23', models.CharField(default='--', max_length=100)),
                ('A23', models.CharField(default='--', max_length=100)),
                ('TO3', models.CharField(default='--', max_length=100)),
                ('E3', models.CharField(default='--', max_length=100)),
                ('SC4', models.CharField(default='--', max_length=100)),
                ('SN4', models.CharField(default='--', max_length=100)),
                ('T14', models.CharField(default='--', max_length=100)),
                ('Q14', models.CharField(default='--', max_length=100)),
                ('A14', models.CharField(default='--', max_length=100)),
                ('T24', models.CharField(default='--', max_length=100)),
                ('Q24', models.CharField(default='--', max_length=100)),
                ('A24', models.CharField(default='--', max_length=100)),
                ('TO4', models.CharField(default='--', max_length=100)),
                ('E4', models.CharField(default='--', max_length=100)),
                ('SC5', models.CharField(default='--', max_length=100)),
                ('SN5', models.CharField(default='--', max_length=100)),
                ('T15', models.CharField(default='--', max_length=100)),
                ('Q15', models.CharField(default='--', max_length=100)),
                ('A15', models.CharField(default='--', max_length=100)),
                ('T25', models.CharField(default='--', max_length=100)),
                ('Q25', models.CharField(default='--', max_length=100)),
                ('A25', models.CharField(default='--', max_length=100)),
                ('TO5', models.CharField(default='--', max_length=100)),
                ('E5', models.CharField(default='--', max_length=100)),
                ('SC6', models.CharField(default='--', max_length=100)),
                ('SN6', models.CharField(default='--', max_length=100)),
                ('T16', models.CharField(default='--', max_length=100)),
                ('Q16', models.CharField(default='--', max_length=100)),
                ('A16', models.CharField(default='--', max_length=100)),
                ('T26', models.CharField(default='--', max_length=100)),
                ('Q26', models.CharField(default='--', max_length=100)),
                ('A26', models.CharField(default='--', max_length=100)),
                ('TO6', models.CharField(default='--', max_length=100)),
                ('E6', models.CharField(default='--', max_length=100)),
                ('SC7', models.CharField(default='--', max_length=100)),
                ('SN7', models.CharField(default='--', max_length=100)),
                ('T17', models.CharField(default='--', max_length=100)),
                ('Q17', models.CharField(default='--', max_length=100)),
                ('A17', models.CharField(default='--', max_length=100)),
                ('T27', models.CharField(default='--', max_length=100)),
                ('Q27', models.CharField(default='--', max_length=100)),
                ('A27', models.CharField(default='--', max_length=100)),
                ('TO7', models.CharField(default='--', max_length=100)),
                ('E7', models.CharField(default='--', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('roll_no', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('ph_no', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('father_name', models.CharField(blank=True, max_length=200, null=True)),
                ('father_no', models.CharField(blank=True, max_length=200, null=True)),
                ('religion', models.CharField(blank=True, max_length=200, null=True)),
                ('caste', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('mtongue', models.CharField(blank=True, max_length=200, null=True)),
                ('bgroup', models.CharField(blank=True, max_length=200, null=True)),
                ('nation', models.CharField(blank=True, max_length=200, null=True)),
                ('hostel', models.CharField(blank=True, max_length=200, null=True)),
                ('morg', models.CharField(blank=True, max_length=200, null=True)),
                ('sports', models.CharField(blank=True, max_length=200, null=True)),
                ('lmark', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sem5',
            name='sid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DIS.student'),
        ),
        migrations.AddField(
            model_name='sem4',
            name='sid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DIS.student'),
        ),
        migrations.AddField(
            model_name='sem3',
            name='sid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DIS.student'),
        ),
        migrations.AddField(
            model_name='sem2',
            name='sid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DIS.student'),
        ),
        migrations.AddField(
            model_name='sem1',
            name='sid',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DIS.student'),
        ),
    ]
