from django.shortcuts import render,redirect
from .models import employee
from .forms import EmployeeForm
def empform(request,id=0):
    if request.method=='GET':
        if id==0:
             form=EmployeeForm()
        else:
             emp=employee.objects.get(pk=id)
             form=EmployeeForm(instance=emp)  
             return render(request,'student/form.html',{'form':form})
    else:
         emp=employee.objects.get(pk=id)
         form=EmployeeForm(request.POST,instance=emp)
         if form.is_valid:
            form.save()
    return redirect('/stud/list')
def emplist(request):
    context={'studentlist':employee.objects.all()}
    return render(request,'student/list.html',context)
def empdelete(request,id):
    emp=employee.objects.get(pk=id)
    emp.delete()
    return redirect('/stud/list')

# Create your views here.
