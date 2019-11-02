from django.db.models import Model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View, generic
from .forms import CategoryModelForm, SubjectModelForm, TeacherModelForm
from .models import Material, Category, Teacher, StudyTable

# Create your views here.
class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {"categories": categories}
        return render(request,'home.html',context)
       

def StudyTable_detail(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        studytable = StudyTable.objects.filter(category=category)
    else:
        studytable = StudyTable.objects.all()    

    context = {
		'category':category,
		'categories':categories,
		'studytable':studytable
	}
    return render(request,'study_table.html',context)

def teacherTable_detail(request,teacher_slug=None):
    teacher = None
    teachers = Teacher.objects.all()
    if teacher_slug:
        teacher = get_object_or_404(Teacher,slug=teacher_slug)
        teachertable = StudyTable.objects.filter(teacher=teacher)
    else:
        teachertable = StudyTable.objects.all()    

    context = {
		'teacher':teacher,
		'teachers':teachers,
		'teachertable':teachertable
	}
    return render(request,'teacher_table.html',context)


def control(request):
    categories = Category.objects.all()
    teachers = Teacher.objects.all()
    materials = Material.objects.all()
    context = {
        'categories': categories,
        'teachers':teachers,
        'materials':materials
    }
    return render(request,'control.html',context)

def category_control(request):
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'control.html',context)

def teachers_control(request):
    teachers = Teacher.objects.all()
    context ={'teachers':teachers}
    return render(request,'control.html',context)

def materials_control(request):
    materials = Material.objects.all()
    context ={'materials':materials}
    return render(request,'control.html',context)    



class AddCategory(View):
    def get(self,request):
        form = CategoryModelForm()
        context = { 'form':form}
        return render(request,'add_category.html',context)

    def post(self,request):
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/control')
        else:
            context = {'form':form}
            return render(request,'add_category.html',context)

class AddMaterial(View):
    def get(self,request):
        form = SubjectModelForm()
        context = { 'form':form}
        return render(request,'add_material.html',context)

    def post(self,request):
        form = SubjectModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/control')
        else:
            context = {'form':form}
            return render(request,'add_material.html',context)

class AddTeacher(View):
    def get(self,request):
        form = TeacherModelForm()
        context = { 'form':form}
        return render(request,'add_teacher.html',context)

    def post(self,request):
        form = TeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/control')
        else:
            context = {'form':form}
            return render(request,'add_teacher.html',context)            

def edit_category(request, pk, template_name='edit_category.html'):
    category= get_object_or_404(Category, pk=pk)
    form = CategoryModelForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('/control')
    return render(request, template_name, {'form':form})

def delete_category(request, pk, template_name='delete_category.html'):
    category= get_object_or_404(Category, pk=pk)    
    if request.method=='POST':
        category.delete()
        return redirect('/control')
    return render(request, template_name, {'object':category})  

def edit_teacher(request, pk, template_name='edit_teacher.html'):
    teacher= get_object_or_404(Teacher, pk=pk)
    form = TeacherModelForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('/control')
    return render(request, template_name, {'form':form})

def delete_teacher(request, pk, template_name='delete_teacher.html'):
    teacher= get_object_or_404(Teacher, pk=pk)    
    if request.method=='POST':
        teacher.delete()
        return redirect('/control')
    return render(request, template_name, {'object':teacher})  

def edit_material(request, pk, template_name='edit_material.html'):
    material= get_object_or_404(Material, pk=pk)
    form = SubjectModelForm(request.POST or None, instance=material)
    if form.is_valid():
        form.save()
        return redirect('/control')
    return render(request, template_name, {'form':form})

def delete_material(request, pk, template_name='delete_material.html'):
    material= get_object_or_404(Material, pk=pk)    
    if request.method=='POST':
        material.delete()
        return redirect('/control')
    return render(request, template_name, {'object':material})                    