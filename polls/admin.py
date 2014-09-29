from django.contrib import admin
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        #('Date Informtion', {'fields': ['pub_date']}),
        ('Date Informtion', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


#class ChoiceAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None, {'fields': ['choice_text', 'question']}),
#    ]

#admin.site.register(Choice, ChoiceAdmin)
#admin.site.register(Choice)
