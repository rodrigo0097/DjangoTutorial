from django.contrib import admin
from .models import Choice, Question


# Register your models here.
"""
El siguiente comando muestra la lista de forma extensa, mientras que el TabularInLine lo muestra mas resumido
en una tabla para crear multiples objetos.
class ChoiceInline(admin.StackedInline):
"""
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #Este param define que columnas se van a mostrar por objeto question
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
