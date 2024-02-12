# Generated by Django 5.0.1 on 2024-02-08 18:25

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0008_rename_true_ans_question_true_answer_test_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='test_app.category'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 18, 18, 25, 9, 656521, tzinfo=datetime.timezone.utc)),
        ),
    ]