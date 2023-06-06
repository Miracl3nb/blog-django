from django import template
import locale

register = template.Library()

@register.filter
def fecha_en_espanol(date):
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
    return date.strftime('%d de %B de %Y')