from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.forms import ModelForm
from .models import Category, StudyTable, Material, Teacher

class CategoryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryModelForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit','إضافة'))
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'القسم' ,
        }

class SubjectModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SubjectModelForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit','إضافة'))
    class Meta:
        model = Material
        fields = '__all__'
        labels = {
            'name': 'المادة' ,
        }

class TeacherModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherModelForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit','إضافة'))
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            'name': 'المدرس',
        }

