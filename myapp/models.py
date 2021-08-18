from django.db import models

# Create your models here.


class employees(models.Model):
    EmpID=models.IntegerField()
    EmpName=models.CharField(max_length=200)
    Age=models.IntegerField()
    Dept=models.CharField(max_length=200)

class Departments(models.Model):
    Dept=models.ForeignKey(
        employees, on_delete=models.CASCADE)
    DeptID=models.IntegerField()

