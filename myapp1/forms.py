from django import forms

from myapp1.models import student_task


class student_form(forms.ModelForm):
    class Meta:
        model = student_task
        fields = ('name','age','department','date','attendance')

        widgets = {
            'date' : forms.widgets.DateInput(attrs={'type' : 'date'})
        }



