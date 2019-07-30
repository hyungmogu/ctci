# ============= Part 1 =============

# Challenge Task 1 of 1
# Add a fieldset containing the 'title', 'order', 'description', and 'content' fields to the TextInline class. Make the 'title' and 'order' fields appear on the same line. Refer to the documentation if you need to

from django.contrib import admin

from . import models

class TextInline(admin.StackedInline):
    model = models.Text

    fieldsets = (
        (None, {
            'fields': (('title', 'order'), 'description', 'content')
        }),
     )

# ============= Part 2 =============

# Challenge Task 1 of 1
# In the TextAdmin class, replace the drop-down menu for the course attribute with radio buttons. The radio buttons should render vertically.

from django.contrib import admin

from . import models

class TextAdmin(admin.ModelAdmin):
    radio_fields = {
        'course': admin.VERTICAL
    }

admin.site.register(models.Text, TextAdmin)



# ============= Part 3 =============

# Challenge Task 1 of 2
# We're doing some housekeeping in our Admin site, and for the moment, we don't want anyone to be able to delete anything. Disable the 'delete_selected' action sitewide. I didn't show you this in the course, so you should check the documentation.

from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.disable_action('delete_selected')


# Challenge Task 2 of 2
# We want to leave the 'delete_selected' action disabled for the rest of the site, but we need to enable it for QuestionAdmin. Can you do that? Again, feel free to check the documentation.

from django.contrib import admin



class QuestionAdmin(admin.ModelAdmin):
    actions = ['delete_selected']


admin.site.disable_action('delete_selected')