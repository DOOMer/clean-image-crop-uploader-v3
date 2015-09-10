# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(max_length=300, upload_to=b'/home/doomer/code/clean-image-crop-uploader/example/media', null=True, verbose_name=b'Main image', blank=True)),
            ],
        ),
    ]
