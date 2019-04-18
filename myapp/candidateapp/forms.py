from django import forms  
from candidateapp.models import Student, Candidate
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__" 		
class StudentForm(forms.ModelForm):  
    class Meta:
        model = Candidate
        fields = "__all__"