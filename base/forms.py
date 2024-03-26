from django import forms
from multiupload.fields import MultiFileField
from .models import Case

class CaseForm(forms.ModelForm):
    images = MultiFileField(max_num=10, min_num=1, max_file_size=1024*1024*5)

    class Meta:
        model = Case
        fields = ['case_number', 'description', 'status', 'images'] 
        labels = {
            'case_number': 'Case Number',
            'description': 'Description',
            'status': 'Status',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'image': forms.FileInput(attrs={'accept': 'image/*'}),
        }
