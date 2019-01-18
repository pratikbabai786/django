from django.shortcuts import render
from pratikapp.models import Employee,Student
from django.db.models import Q
from django.db.models import Min,Max,Avg,Sum
from django.db.models.functions import Lower



def home(request):
    student=Student.objects.all().order_by(Lower('name'))



    return render(request,'pratikapp/wish.html',{'student':student})


def operation(request):

    max=Student.objects.all().aggregate(Max('marks'))
    min=Student.objects.all().aggregate(Min('marks'))
    avg=Student.objects.all().aggregate(Avg('marks'))
    sum=Student.objects.all().aggregate(Sum('marks'))
    dict={'max':max,'min':min,'avg':avg,'sum':sum}
    return render(request,'pratikapp/wish1.html',context=dict)
