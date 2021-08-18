from django.shortcuts import render
from .models import employees,Departments
# Create your views here.










def title(request):
    return render(request,'title.html')

def index(request):
    
    if request.method == 'POST':
        EmpID= request.POST['emid']
        empname=request.POST['empname']
        age= request.POST['age']
        dept= request.POST['dept']


        form=employees(EmpID=EmpID,EmpName=empname,Age=age,Dept=dept)
        form.save()
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def show(request):
    if request.method == 'POST':
        EmpID= request.POST['emid']
        context={"obj2":"No Records"}
        if (employees.objects.filter(EmpID=EmpID)).exists():
            obj1=employees.objects.get(EmpID=EmpID)
            context={
            "obj1":obj1
            }
            return render(request,"show.html",context)
        else:
            return render(request,"show.html",context)
    else:
        obj=employees.objects.all()
        context={
            "obj":obj,
        }
        obj.order_by("EmpID")
        return render(request,"show.html",context)

def delete(request):
    if request.method == 'POST':
        EmpID= request.POST['emid']
        emp=employees.objects.get(EmpID=EmpID)
        emp.delete()
        return render(request,'title.html')
    else:
        return render(request,'delete.html')
def change(request):
    if request.method == 'POST':
        EmpID= request.POST['empid']
        dept= request.POST['dept']
        emp=employees.objects.get(EmpID=EmpID)
        emp.Dept=dept
        emp.save()
        return render(request,'title.html')
    else:
        return render(request,'edit.html')

