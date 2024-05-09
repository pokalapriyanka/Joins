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

def selfjoins(request):

    MEJD=Emp.objects.select_related('Mgr').all()
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Emp_name='Smith')
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Emp_no=2222)
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Emp_name__contains='i')
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Commi__isnull=True)
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Sal__gte=2000)
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Hiredate__year='2023')
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Emp_name='Allen')
    MEJD=Emp.objects.select_related('Mgr').filter(Mgr__Emp_name__startswith='S')


    d={'MEJD':MEJD}
    return render(request,'selfjoins.html',d)