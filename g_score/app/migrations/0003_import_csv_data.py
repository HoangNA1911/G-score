# Generated by Django 4.2.3 on 2024-12-27 11:11
import csv
from django.db import migrations, transaction
import pandas as pd


def import_csv_data(apps, schema_editor):

    Student = apps.get_model('app', 'Student')

    csv_file_path = '/Users/huyna/Documents/G-Score/g_score/diem_thi_thpt_2024.csv'

    df = pd.read_csv(csv_file_path)

    # Replace empty strings with None (null)
    df = df.replace('', None)
    with open(csv_file_path, 'r') as file:
        with transaction.atomic():
            student = [
                Student(
                    sbd=row['sbd'],
                    toan=row['toan'],
                    ngu_van=row['ngu_van'],
                    ngoai_ngu=row['ngoai_ngu'],
                    vat_ly=row['vat_li'],
                    hoa_hoc=row['hoa_hoc'],
                    sinh_hoc=row['sinh_hoc'],
                    lich_su=row['lich_su'],
                    dia_ly=row['dia_li'],
                    gdcd=row['gdcd'],
                    ma_ngoai_ngu=row['ma_ngoai_ngu']
                )
                for _, row in df.iterrows()
            ]
            Student.objects.bulk_create(student)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_student_gdcd'),
    ]

    operations = [
        migrations.RunPython(import_csv_data),
    ]
