# ============= Part 1 =============
# Challenge Task 1 of 1
# Register the Course model from models.py and the CourseAdmin class with the admin.

from django.contrib import admin

from . import models


class TextInline(admin.StackedInline):
    model = models.Text


class QuizInline(admin.StackedInline):
    model = models.Quiz


class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]


admin.site.register(models.Course, CourseAdmin)


# ============= Part 2 =============
# Challenge Task 1 of 2
# Create a new ModelAdmin named TextAdmin. In TextAdmin, create a fields attribute in this order: 'course', 'title', 'order', and finally 'description'.
from django.contrib import admin

from . import models

class TextAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'order', 'description']

admin.site.register(models.Text)


# Challenge Task 2 of 2
# Now change the models.Text registration so it uses your TextAdmin class.
from django.contrib import admin

from . import models

class TextAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'order', 'description']

admin.site.register(models.Text, TextAdmin)
