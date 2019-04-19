from django import forms  
from candidateapp.models import Student, Candidate
from localflavor.in_.forms import INAadhaarNumberField
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__" 		
class StudentForm(forms.ModelForm):  
    class Meta:
        model = Candidate
        fields = "__all__"
      