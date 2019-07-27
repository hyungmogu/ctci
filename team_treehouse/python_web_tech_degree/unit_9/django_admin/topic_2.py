# ============= Part 1 =============
# Challenge Task 1 of 2
# Add the ability to filter by 'course' to the QuizAdmin class.

from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']
    list_filter = ['course']

admin.site.register(models.Quiz, QuizAdmin)


# Challenge Task 2 of 2
# Now add a search box to the QuizAdmin class, and make sure the searched text scans the 'title' and 'description' attributes.


from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
    fields = ['course', 'title', 'description', 'order', 'total_questions']
    list_filter = ['course']
    search_fields = ['title', 'description']

admin.site.register(models.Quiz, QuizAdmin)



# ============= Part 2 =============
# Challenge Task 1 of 4
# We're going to create a custom filter for 'topic' for the Course model. Before the CourseAdmin class definition, set up a TopicListFilter class for your filter. Set the title attribute to "topic". You'll need to set the parameter_name attribute, too, but I'm sure you can figure out which attribute we're filtering on.

from django.contrib import admin

from . import models

class TextInline(admin.StackedInline):
    model = models.Text

class QuizInline(admin.StackedInline):
    model = models.Quiz

class AnswerInline(admin.StackedInline):
    model = models.Answer

class TopicListFilter(admin.SimpleListFilter):
    # ENTER YOUR CODE HERE.
    title = 'topic'
    parameter_name = 'topic'

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]

    list_filter = ['created_at', 'is_live']

admin.site.register(models.Course, CourseAdmin)

