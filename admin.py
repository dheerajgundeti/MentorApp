from django.contrib import admin

from .models import College,Student,MockTest1,Teacher

admin.site.register(College)
admin.site.register(Student)
admin.site.register(MockTest1)
admin.site.register(Teacher)