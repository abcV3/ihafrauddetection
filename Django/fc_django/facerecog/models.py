from django.db import models

# Create your models here.

class InsDetails(models.Model):

    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)

    class Meta:
        db_table = "InsDetails"
"""class EmpDetails(models.Model):

    firstname=models.CharField(max_length=256)
    lastname=models.CharField(max_length=256)

    class Meta:
        db_table = "EmpDetails"

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    eid = models.IntegerField()
    attendance = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Attendance" """