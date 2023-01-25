from django.contrib import admin
from admission.models import student
from admission.models import Teacher


class studentAdmin(admin.ModelAdmin):
    list_display=['id','name','fathername','classname','contact']
class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','experience','subject','contact']
# Register your models here.
admin.site.register(student, studentAdmin)
admin.site.register(Teacher, TeacherAdmin)
