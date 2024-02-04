from django import forms
from .models import Course
from .models import CourseData

class CourseForm(forms.ModelForm):

    generate_enrollment_key = forms.BooleanField(required=False, label='Generate Enrollment Key')

    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }

class CourseDataForm(forms.ModelForm):

    class Meta:
        model = CourseData
        fields = ['title','file','description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
