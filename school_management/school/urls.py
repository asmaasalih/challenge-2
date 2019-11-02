from django.conf.urls import url
from django.urls import path, re_path
from . import views
from .views import HomePageView, StudyTable_detail, teacherTable_detail, edit_material, edit_teacher, delete_material, delete_teacher, control, category_control, edit_category, delete_category, materials_control, teachers_control, AddCategory, AddMaterial, AddTeacher


urlpatterns = [
    path('',HomePageView.as_view(),name='home-page'),
    path('studytable/',views.StudyTable_detail,name='studytable'),
    path('control/',views.control,name='control'),
    path('teachertable/',views.teacherTable_detail,name='teachertable'),
    url(r'^teachertable/(?P<teacher_slug>[-\w]+)/$',views.teacherTable_detail,name='teacher'),
    path('categories/add_category/',AddCategory.as_view(),name='add_category'),
    path('categories/edit_category/<int:pk>/',views.edit_category,name='edit_category'),
    path('categories/delete_category/<int:pk>/',views.delete_category,name='delete_category'),
    path('materials/add_material/',AddMaterial.as_view(),name='add_material'),
    path('materials/edit_material/<int:pk>/',views.edit_material,name='edit_material'),
    path('materials/delete_material/<int:pk>/',views.delete_material,name='delete_material'),
    path('teachers/add_teacher/',AddTeacher.as_view(),name='add_teacher'),
    path('teachers/edit_teacher/<int:pk>/',views.edit_teacher,name='edit_teacher'),
    path('teachers/delete_teacher/<int:pk>/',views.delete_teacher,name='delete_teacher'),
    path('control/categories/',views.category_control,name='categories'),
    path('teachers/',views.teachers_control,name='teachers'),
    path('materials/',views.materials_control,name='materials'),
    url(r'^studytable/(?P<category_slug>[-\w]+)/$',views.StudyTable_detail,name='studycategory'),
]
