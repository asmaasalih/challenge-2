from django.contrib import admin
from .models import Material, Category, Teacher, StudyTable

# Register your models here.
admin.site.register(Material)
admin.site.register(Teacher)
admin.site.register(Category)
admin.site.register(StudyTable)


