from django.db import models


# Create your models here.

class Student(models.Model):
    sbd = models.IntegerField(primary_key=True)

    toan = models.FloatField(null=True, blank=True)

    ngu_van = models.FloatField(null=True, blank=True)

    ngoai_ngu = models.FloatField(null=True, blank=True)

    vat_ly = models.FloatField(null=True, blank=True)

    hoa_hoc = models.FloatField(null=True, blank=True)

    sinh_hoc = models.FloatField(null=True, blank=True)

    lich_su = models.FloatField(null=True, blank=True)

    dia_ly = models.FloatField(null=True, blank=True)

    gdcd = models.FloatField(null=True, blank=True)

    ma_ngoai_ngu = models.CharField(max_length=5)

    def total_a_group_score(self):

        return self.toan+self.hoa_hoc+self.vat_ly


