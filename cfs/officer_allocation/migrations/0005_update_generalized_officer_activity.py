# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import migrations, models

base_dir = os.path.realpath(os.path.dirname(__file__))

def sql_path(filename):
    return os.path.join(base_dir, "sql", filename)

with open(sql_path("generalized_officer_activity2.sql")) as f:
    officer_activity_sql = f.read()

class Migration(migrations.Migration):

    dependencies = [
        ('officer_allocation', '0004_auto_20161212_1657'),
    ]

    operations = [
        migrations.RunSQL(officer_activity_sql),
    ]
