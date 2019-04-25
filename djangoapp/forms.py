from django import forms  
from djangoapp.models import Student
from localflavor.in_.forms import INAadhaarNumberField
  
class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = "__all__" 