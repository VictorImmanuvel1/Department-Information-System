# Generated by Django 2.1.7 on 2021-04-21 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DIS', '0003_auto_20210421_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='ap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph1', models.CharField(default=0, max_length=200)),
                ('y1', models.CharField(default=0, max_length=200)),
                ('ph2', models.CharField(default=0, max_length=200)),
                ('y2', models.CharField(default=0, max_length=200)),
                ('ph3', models.CharField(default=0, max_length=200)),
                ('y3', models.CharField(default=0, max_length=200)),
                ('ph4', models.CharField(default=0, max_length=200)),
                ('y4', models.CharField(default=0, max_length=200)),
                ('ph5', models.CharField(default=0, max_length=200)),
                ('y5', models.CharField(default=0, max_length=200)),
                ('ph6', models.CharField(default=0, max_length=200)),
                ('y6', models.CharField(default=0, max_length=200)),
                ('ph7', models.CharField(default=0, max_length=200)),
                ('y7', models.CharField(default=0, max_length=200)),
                ('ph8', models.CharField(default=0, max_length=200)),
                ('y8', models.CharField(default=0, max_length=200)),
                ('ph9', models.CharField(default=0, max_length=200)),
                ('y9', models.CharField(default=0, max_length=200)),
                ('ph10', models.CharField(default=0, max_length=200)),
                ('y10', models.CharField(default=0, max_length=200)),
                ('ph11', models.CharField(default=0, max_length=200)),
                ('y11', models.CharField(default=0, max_length=200)),
                ('ph12', models.CharField(default=0, max_length=200)),
                ('y12', models.CharField(default=0, max_length=200)),
                ('ph13', models.CharField(default=0, max_length=200)),
                ('y13', models.CharField(default=0, max_length=200)),
                ('ph14', models.CharField(default=0, max_length=200)),
                ('y14', models.CharField(default=0, max_length=200)),
                ('ph15', models.CharField(default=0, max_length=200)),
                ('y15', models.CharField(default=0, max_length=200)),
                ('ph16', models.CharField(default=0, max_length=200)),
                ('y16', models.CharField(default=0, max_length=200)),
                ('ph17', models.CharField(default=0, max_length=200)),
                ('y17', models.CharField(default=0, max_length=200)),
                ('ph18', models.CharField(default=0, max_length=200)),
                ('y18', models.CharField(default=0, max_length=200)),
                ('ph19', models.CharField(default=0, max_length=200)),
                ('y19', models.CharField(default=0, max_length=200)),
                ('ph20', models.CharField(default=0, max_length=200)),
                ('y20', models.CharField(default=0, max_length=200)),
                ('ph21', models.CharField(default=0, max_length=200)),
                ('y21', models.CharField(default=0, max_length=200)),
                ('ph22', models.CharField(default=0, max_length=200)),
                ('y22', models.CharField(default=0, max_length=200)),
                ('ph23', models.CharField(default=0, max_length=200)),
                ('y23', models.CharField(default=0, max_length=200)),
                ('ph24', models.CharField(default=0, max_length=200)),
                ('y24', models.CharField(default=0, max_length=200)),
                ('ph25', models.CharField(default=0, max_length=200)),
                ('y25', models.CharField(default=0, max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t1', models.CharField(default=0, max_length=200)),
                ('y1', models.CharField(default=0, max_length=200)),
                ('j1', models.CharField(default=0, max_length=200)),
                ('n1', models.CharField(default=0, max_length=200)),
                ('t2', models.CharField(default=0, max_length=200)),
                ('y2', models.CharField(default=0, max_length=200)),
                ('j2', models.CharField(default=0, max_length=200)),
                ('n2', models.CharField(default=0, max_length=200)),
                ('t3', models.CharField(default=0, max_length=200)),
                ('y3', models.CharField(default=0, max_length=200)),
                ('j3', models.CharField(default=0, max_length=200)),
                ('n3', models.CharField(default=0, max_length=200)),
                ('t4', models.CharField(default=0, max_length=200)),
                ('y4', models.CharField(default=0, max_length=200)),
                ('j4', models.CharField(default=0, max_length=200)),
                ('n4', models.CharField(default=0, max_length=200)),
                ('t5', models.CharField(default=0, max_length=200)),
                ('y5', models.CharField(default=0, max_length=200)),
                ('j5', models.CharField(default=0, max_length=200)),
                ('n5', models.CharField(default=0, max_length=200)),
                ('t6', models.CharField(default=0, max_length=200)),
                ('y6', models.CharField(default=0, max_length=200)),
                ('j6', models.CharField(default=0, max_length=200)),
                ('n6', models.CharField(default=0, max_length=200)),
                ('t7', models.CharField(default=0, max_length=200)),
                ('y7', models.CharField(default=0, max_length=200)),
                ('j7', models.CharField(default=0, max_length=200)),
                ('n7', models.CharField(default=0, max_length=200)),
                ('t8', models.CharField(default=0, max_length=200)),
                ('y8', models.CharField(default=0, max_length=200)),
                ('j8', models.CharField(default=0, max_length=200)),
                ('n8', models.CharField(default=0, max_length=200)),
                ('t9', models.CharField(default=0, max_length=200)),
                ('y9', models.CharField(default=0, max_length=200)),
                ('j9', models.CharField(default=0, max_length=200)),
                ('n9', models.CharField(default=0, max_length=200)),
                ('t10', models.CharField(default=0, max_length=200)),
                ('y10', models.CharField(default=0, max_length=200)),
                ('j10', models.CharField(default=0, max_length=200)),
                ('n10', models.CharField(default=0, max_length=200)),
                ('t11', models.CharField(default=0, max_length=200)),
                ('y11', models.CharField(default=0, max_length=200)),
                ('j11', models.CharField(default=0, max_length=200)),
                ('n11', models.CharField(default=0, max_length=200)),
                ('t12', models.CharField(default=0, max_length=200)),
                ('y12', models.CharField(default=0, max_length=200)),
                ('j12', models.CharField(default=0, max_length=200)),
                ('n12', models.CharField(default=0, max_length=200)),
                ('t13', models.CharField(default=0, max_length=200)),
                ('y13', models.CharField(default=0, max_length=200)),
                ('j13', models.CharField(default=0, max_length=200)),
                ('n13', models.CharField(default=0, max_length=200)),
                ('t14', models.CharField(default=0, max_length=200)),
                ('y14', models.CharField(default=0, max_length=200)),
                ('j14', models.CharField(default=0, max_length=200)),
                ('n14', models.CharField(default=0, max_length=200)),
                ('t15', models.CharField(default=0, max_length=200)),
                ('y15', models.CharField(default=0, max_length=200)),
                ('j15', models.CharField(default=0, max_length=200)),
                ('n15', models.CharField(default=0, max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='oe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.CharField(default=0, max_length=200)),
                ('i1', models.CharField(default=0, max_length=200)),
                ('y1', models.CharField(default=0, max_length=200)),
                ('d2', models.CharField(default=0, max_length=200)),
                ('i2', models.CharField(default=0, max_length=200)),
                ('y2', models.CharField(default=0, max_length=200)),
                ('d3', models.CharField(default=0, max_length=200)),
                ('i3', models.CharField(default=0, max_length=200)),
                ('y3', models.CharField(default=0, max_length=200)),
                ('d4', models.CharField(default=0, max_length=200)),
                ('i4', models.CharField(default=0, max_length=200)),
                ('y4', models.CharField(default=0, max_length=200)),
                ('d5', models.CharField(default=0, max_length=200)),
                ('i5', models.CharField(default=0, max_length=200)),
                ('y5', models.CharField(default=0, max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seminar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w1', models.CharField(default=0, max_length=200)),
                ('t1', models.CharField(default=0, max_length=200)),
                ('y1', models.CharField(default=0, max_length=200)),
                ('i1', models.CharField(default=0, max_length=200)),
                ('n1', models.CharField(default=0, max_length=200)),
                ('w2', models.CharField(default=0, max_length=200)),
                ('t2', models.CharField(default=0, max_length=200)),
                ('y2', models.CharField(default=0, max_length=200)),
                ('i2', models.CharField(default=0, max_length=200)),
                ('n2', models.CharField(default=0, max_length=200)),
                ('w3', models.CharField(default=0, max_length=200)),
                ('t3', models.CharField(default=0, max_length=200)),
                ('y3', models.CharField(default=0, max_length=200)),
                ('i3', models.CharField(default=0, max_length=200)),
                ('n3', models.CharField(default=0, max_length=200)),
                ('w4', models.CharField(default=0, max_length=200)),
                ('t4', models.CharField(default=0, max_length=200)),
                ('y4', models.CharField(default=0, max_length=200)),
                ('i4', models.CharField(default=0, max_length=200)),
                ('n4', models.CharField(default=0, max_length=200)),
                ('w5', models.CharField(default=0, max_length=200)),
                ('t5', models.CharField(default=0, max_length=200)),
                ('y5', models.CharField(default=0, max_length=200)),
                ('i5', models.CharField(default=0, max_length=200)),
                ('n5', models.CharField(default=0, max_length=200)),
                ('w6', models.CharField(default=0, max_length=200)),
                ('t6', models.CharField(default=0, max_length=200)),
                ('y6', models.CharField(default=0, max_length=200)),
                ('i6', models.CharField(default=0, max_length=200)),
                ('n6', models.CharField(default=0, max_length=200)),
                ('w7', models.CharField(default=0, max_length=200)),
                ('t7', models.CharField(default=0, max_length=200)),
                ('y7', models.CharField(default=0, max_length=200)),
                ('i7', models.CharField(default=0, max_length=200)),
                ('n7', models.CharField(default=0, max_length=200)),
                ('w8', models.CharField(default=0, max_length=200)),
                ('t8', models.CharField(default=0, max_length=200)),
                ('y8', models.CharField(default=0, max_length=200)),
                ('i8', models.CharField(default=0, max_length=200)),
                ('n8', models.CharField(default=0, max_length=200)),
                ('w9', models.CharField(default=0, max_length=200)),
                ('t9', models.CharField(default=0, max_length=200)),
                ('y9', models.CharField(default=0, max_length=200)),
                ('i9', models.CharField(default=0, max_length=200)),
                ('n9', models.CharField(default=0, max_length=200)),
                ('w10', models.CharField(default=0, max_length=200)),
                ('t10', models.CharField(default=0, max_length=200)),
                ('y10', models.CharField(default=0, max_length=200)),
                ('i10', models.CharField(default=0, max_length=200)),
                ('n10', models.CharField(default=0, max_length=200)),
                ('w11', models.CharField(default=0, max_length=200)),
                ('t11', models.CharField(default=0, max_length=200)),
                ('y11', models.CharField(default=0, max_length=200)),
                ('i11', models.CharField(default=0, max_length=200)),
                ('n11', models.CharField(default=0, max_length=200)),
                ('w12', models.CharField(default=0, max_length=200)),
                ('t12', models.CharField(default=0, max_length=200)),
                ('y12', models.CharField(default=0, max_length=200)),
                ('i12', models.CharField(default=0, max_length=200)),
                ('n12', models.CharField(default=0, max_length=200)),
                ('w13', models.CharField(default=0, max_length=200)),
                ('t13', models.CharField(default=0, max_length=200)),
                ('y13', models.CharField(default=0, max_length=200)),
                ('i13', models.CharField(default=0, max_length=200)),
                ('n13', models.CharField(default=0, max_length=200)),
                ('w14', models.CharField(default=0, max_length=200)),
                ('t14', models.CharField(default=0, max_length=200)),
                ('y14', models.CharField(default=0, max_length=200)),
                ('i14', models.CharField(default=0, max_length=200)),
                ('n14', models.CharField(default=0, max_length=200)),
                ('w15', models.CharField(default=0, max_length=200)),
                ('t15', models.CharField(default=0, max_length=200)),
                ('y15', models.CharField(default=0, max_length=200)),
                ('i15', models.CharField(default=0, max_length=200)),
                ('n15', models.CharField(default=0, max_length=200)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]