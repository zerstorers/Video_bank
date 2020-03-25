{from modeltranslation.translator import translator, TranslationOptions
from .models import Movies

class NewsTranslationOptions(TranslationOptions):
    fields = ('description')

translator.register(, NewsTranslationOptions)}