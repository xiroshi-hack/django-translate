from dataclasses import field
from modeltranslation.translator import register, TranslationOptions
from .models import TranslatePage

@register(TranslatePage)
class MalumotTranslateOption(TranslationOptions):
    fields = ('name', 'title',)