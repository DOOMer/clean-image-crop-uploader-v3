# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('file', models.FileField(upload_to=b'ajax_uploads/', verbose_name='file')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'uploaded file',
                'verbose_name_plural': 'uploaded files',
            },
        ),
    ]
