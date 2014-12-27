# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141226_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
            preserve_default=True,
        ),
    ]
