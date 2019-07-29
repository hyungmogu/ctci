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


# Challenge Task 2 of 4
# Add the lookups method to your TopicListFilter. Remember that this method takes self, request, and model_admin as arguments, and that you need to return a tuple of tuples.

# For the tuples, add "Python", "Ruby", and "Java" as options and values. See the documentation if you get lost.


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

    def lookups(self, request, model_admin):
        return (
            ('python', 'Python'),
            ('ruby', 'Ruby'),
            ('java', 'Java')
        )

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]

    list_filter = ['created_at', 'is_live']

admin.site.register(models.Course, CourseAdmin)


# Challenge Task 3 of 4
# Create the queryset method. Remember that this method takes in self, request, and queryset as arguments. In the method, check to see if self.value() returns anything. If it does, .filter() the queryset for records where the title contains the value. Use contains for the comparison.


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

    def lookups(self, request, model_admin):
        return (
            ('python', 'Python'),
            ('ruby', 'Ruby'),
            ('java', 'Java')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__contains=self.value())

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]

    list_filter = ['created_at', 'is_live']

admin.site.register(models.Course, CourseAdmin)


# Challenge Task 4 of 4
# Finally, add your custom filter to the CourseAdmin's list_filter attribute.

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

    def lookups(self, request, model_admin):
        return (
            ('python', 'Python'),
            ('ruby', 'Ruby'),
            ('java', 'Java')
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__contains=self.value())

class CourseAdmin(admin.ModelAdmin):
    inlines = [TextInline, QuizInline]

    list_filter = ['created_at', 'is_live', TopicListFilter]

admin.site.register(models.Course, CourseAdmin)

# ============= Part 3 =============
# Challenge Task 1 of 2
# Add a method to the Quiz model, named number_correct_needed that returns a string showing the number of correct answers needed to get at least 70% on the quiz. Your string should include the number needed and the total number. An example would be "7/10".

# Use the ceil function in the math module which has already been imported for you.

# courses/models.py
from django.db import models
import math

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title

class Quiz(Step):
    total_questions = models.IntegerField()

    def number_correct_needed(self):

        return '{0}/{1}'.format(math.ceil(self.total_questions*0.7), self.total_questions)


# courses/admin.py

from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']

# Challenge Task 2 of 2
# Now add your new number_correct_needed method to the list_display attribute on the QuizAdmin class in admin.py.


# courses/models.py
from django.db import models
import math

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title

class Quiz(Step):
    total_questions = models.IntegerField()

    def number_correct_needed(self):

        return '{0}/{1}'.format(math.ceil(self.total_questions*0.7), self.total_questions)


# courses/admin.py

from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'number_correct_needed']

# ============= Part 4 =============

# Challenge Task 1 of 1
# Make 'course' and 'total_questions' editable fields in the list view for the QuizAdmin class.

from django.contrib import admin

from . import models

class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'total_questions', 'number_correct_needed']
    list_editable = ['course', 'total_questions']

admin.site.register(models.Quiz, QuizAdmin)



