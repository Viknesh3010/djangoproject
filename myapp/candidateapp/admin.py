from django.contrib import admin
from .models import Candidate, Student
class CandidateAdmin(admin.ModelAdmin):
    pass
class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Candidate,CandidateAdmin)
admin.site.register(Student,StudentAdmin)


# Register your models here.
