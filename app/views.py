from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.
def innerEquijoins(request):

    JDED=Emp.objects.select_related('Deptno').all()
    JDED=Emp.objects.select_related('Deptno').filter(Emp_name='Smith')
    JDED=Emp.objects.select_related('Deptno').filter(Deptno__D_name='Accounting')
    JDED=Emp.objects.select_related('Deptno').filter(Sal__gte=2000)
    JDED=Emp.objects.select_related('Deptno').filter(Hiredate__year__gt='2023')
    JDED=Emp.objects.select_related('Deptno').filter(Deptno__D_loc='Dallas')
    JDED=Emp.objects.select_related('Deptno').filter(Commi__lte=200)
    JDED=Emp.objects.select_related('Deptno').filter(Emp_name__startswith='A')
    JDED=Emp.objects.select_related('Deptno').filter(Emp_name__endswith='n')
    JDED=Emp.objects.select_related('Deptno').filter(Emp_name__contains='e')
    JDED=Emp.objects.select_related('Deptno').filter(Deptno=20)
    JDED=Emp.objects.select_related('Deptno').filter(Deptno__D_name='Developer')
    JDED=Emp.objects.select_related('Deptno').filter(Hiredate__month__gt='3')
    JDED=Emp.objects.select_related('Deptno').filter(Commi__isnull=False)
    JDED=Emp.objects.select_related('Deptno').filter(Emp_no__in=[1111,5555])
    JDED=Emp.objects.select_related('Deptno').filter(Hiredate__year__gt='2023')
    JDED=Emp.objects.select_related('Deptno').filter(Emp_name__in=['Allen','Smith'])
    #JDED=Emp.objects.select_related('Deptno').filter(Mgr='Smith')
    JDED=Emp.objects.select_related('Deptno').filter(Q(Deptno=10) | Q(Deptno=20))
    JDED=Emp.objects.select_related('Deptno').filter(Q(Deptno=10) | Q(Deptno=20) & Q(Deptno__D_name='Research'))
    JDED=Emp.objects.select_related('Deptno').filter(job='Clerk',Emp_name__endswith='h')
    JDED=Emp.objects.select_related('Deptno').filter(Sal__lte=2500,Deptno=20)
    





    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)