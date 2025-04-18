from django import forms
from .models import usermodel
from .models import coursemodel
from .models import subjectmodel
from .models import papermodel


class userform(forms.ModelForm):
    class Meta:
        model = usermodel
        fields=['name','dob','mobile_number','email','userid','password','gender']
        widgets = {
            'gender': forms.RadioSelect,
            'dob':forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'password':forms.PasswordInput,
        }

class subjectform(forms.ModelForm):
    class Meta:
        model = subjectmodel
        fields="__all__"
       
class courseform(forms.ModelForm):
    class Meta:
        model = coursemodel
        fields="__all__"
            
class paperform(forms.ModelForm):
    class Meta:
        model = papermodel
        fields="__all__"
            
            
