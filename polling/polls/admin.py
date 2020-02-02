from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "Polling Admin"
admin.site.site_title = "Polling Admin Area"
admin.site.index_title = "Welcome to the Polling Admin Panel"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra_fields = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [ 
        (None, { 'fields': ['question_text'] }),
        ( 'Date Information', { 'fields': ['publish_date'], 'classes': ['collapse'] } ), 
    ]

    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)