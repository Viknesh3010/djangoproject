from django.contrib import admin
from .models import Student, Student_Language, Language, Skill, Skill_Categories, Student_Skill, Student_Certificate, Student_Academics,Student_Employment_History, Visa_Categories, Student_Visa,Student_Passport
class StudentAdmin(admin.ModelAdmin):
    pass
class LanguageAdmin(admin.ModelAdmin):
    pass
class Languages(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass
class SkillCategoryAdmin(admin.ModelAdmin):
    pass
class StudentSkillAdmin(admin.ModelAdmin):
    pass
class StudentCertificateAdmin(admin.ModelAdmin):
    pass
class StudentAcademicsAdmin(admin.ModelAdmin):
    pass
class StudentEmploymentAdmin(admin.ModelAdmin):
    pass
class VisaCategoryAdmin(admin.ModelAdmin):
    pass
class StudentVisaAdmin(admin.ModelAdmin): 
    pass
class StudentPassportAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student,StudentAdmin)
admin.site.register(Student_Language,LanguageAdmin)
admin.site.register(Language, Languages)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Skill_Categories,SkillCategoryAdmin)
admin.site.register(Student_Skill, StudentSkillAdmin)
admin.site.register(Student_Certificate,StudentCertificateAdmin)
admin.site.register(Student_Academics, StudentAcademicsAdmin)
admin.site.register(Student_Employment_History,StudentEmploymentAdmin)
admin.site.register(Visa_Categories,VisaCategoryAdmin)
admin.site.register(Student_Visa, StudentVisaAdmin)
admin.site.register(Student_Passport, StudentPassportAdmin)