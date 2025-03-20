from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)
    icon = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
      return f"{self.name}"

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses")
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=1000)
    
    def __str__(self):
      return f"{self.name}"
      

class NestedLesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="nested_lesaon")
    name = models.CharField(max_length=300)
    icon = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
      return f"{self.name}"

'''class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons",null=True, blank=True)
    nested_lesaon = models.ForeignKey(NestedLesson, on_delete=models.CASCADE, related_name="nested_lessons",null=True, blank=True)
    name = models.CharField(max_length=300)
    content = models.TextField(null=True, blank=True)'''
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons", null=True, blank=True)
    nested_lesaon = models.ForeignKey(NestedLesson, on_delete=models.CASCADE, related_name="nested_lessons", null=True, blank=True)
    name = models.CharField(max_length=300)
    content = MarkdownxField(null=True, blank=True)

    def related_entity(self):
        if self.course:
            return f"Course: {self.course.name}"
        elif self.nested_lesaon:
            return f"Nested Lesson: {self.nested_lesaon.name}"
        return "No related entity"

    def clean(self):
        if self.course and self.nested_lesaon:
            raise ValidationError("Lesson can only be related to either Course or NestedLesson, not both.")
        if not self.course and not self.nested_lesaon:
            raise ValidationError("Lesson must be related to either a Course or a NestedLesson.")

    def __str__(self):
        return f"{self.name}"
    
