from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Admin)
admin.site.register(University)
admin.site.register(Professor)  
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grades)
admin.site.register(Registration)