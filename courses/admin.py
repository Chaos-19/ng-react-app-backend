from django.contrib import admin
from .models import Category,NestedLesson, Course, Lesson
from markdownx.admin import MarkdownxModelAdmin 

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","icon","slug"]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name","icon","category"]

@admin.register(NestedLesson) 
class NestedLessonAdmin(admin.ModelAdmin):
    list_display = ["name","icon","slug"]
  
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'related_entity', 'content')
    fieldsets = [
      (None,{"fields":["name"]}),
      ("Lesson content",{"fields":["content"]}),
      ("parent",{"fields":["nested_lesaon"]}),
      ("parent",{"fields":["course"]}),
    ]