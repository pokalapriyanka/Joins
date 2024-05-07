from django.db import models

# Create your models here.
class Dept(models.Model):
    D_deptno=models.IntegerField(primary_key=True)
    D_loc=models.CharField(max_length=20,unique=100)
    D_name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.D_deptno)



class Emp(models.Model):
    Emp_no=models.IntegerField(max_length=20,primary_key=True)
    Emp_name=models.CharField(max_length=20)
    job=models.CharField(max_length=100)
    Sal=models.DecimalField(max_digits=8,decimal_places=2)
    Mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    Commi=models.DecimalField(max_digits=8,decimal_places=2)
    Hiredate=models.DateField()
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.Emp_name

class Salgrade(models.Model):
    Grade=models.IntegerField(primary_key=True)
    Hisal=models.DecimalField(max_digits=8,decimal_places=2)
    Losal=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return str(self.Grade)
