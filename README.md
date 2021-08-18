myproject->myapp->models.py 

from django.db import models

class employees(models.Model):  // created new employees and departments and respective cloumns.
    EmpID=models.IntegerField() 
    EmpName=models.CharField(max_length=200)
    Age=models.IntegerField()
    Dept=models.CharField(max_length=200)

class Departments(models.Model):
    Dept=models.ForeignKey(                     //Foreign key to connect department and employees
        employees, on_delete=models.CASCADE)
    DeptID=models.IntegerField()


myapp->views.py

from django.shortcuts import render
from .models import employees,Departments
# Create your views here.

def title(request): 
    return render(request,'title.html')

def index(request):  
    
    if request.method == 'POST': //form to get the values from front end and storing in postgreDB 
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
    if request.method == 'POST':  //searching for certain record form the databases
        EmpID= request.POST['emid']
        context={"obj2":"No Records"}
        if (employees.objects.filter(EmpID=EmpID)).exists(): // checking the given input in databases
            obj1=employees.objects.get(EmpID=EmpID)
            context={
            "obj1":obj1
            }
            return render(request,"show.html",context)
        else:
            return render(request,"show.html",context)
    else:                                                     // showing all record in sorting 
        obj=employees.objects.all()
        context={
            "obj":obj,
        }
        obj.order_by("EmpID")
        return render(request,"show.html",context)

def delete(request):                                         // delete the record by employee_id 
    if request.method == 'POST':
        EmpID= request.POST['emid']
        emp=employees.objects.get(EmpID=EmpID)
        emp.delete()
        return render(request,'title.html')
    else:
        return render(request,'delete.html')
def change(request):                                         //change department by given empid
    if request.method == 'POST':
        EmpID= request.POST['empid']
        dept= request.POST['dept']
        emp=employees.objects.get(EmpID=EmpID)
        emp.Dept=dept
        emp.save()
        return render(request,'title.html')
    else:
        return render(request,'edit.html')  
        
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  //connection of django to postgresql
        'NAME': 'employers',
        'USER':'postgres',
        'PASSWORD':'******',
        'HOST':'localhost',
        'PORT':'5432'
    }
}
