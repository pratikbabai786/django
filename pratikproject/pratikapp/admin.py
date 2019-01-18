from django.contrib import admin
from pratikapp.models import Student,Employee

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','no','marks']

admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','no','sal']

admin.site.register(Employee,EmployeeAdmin)
