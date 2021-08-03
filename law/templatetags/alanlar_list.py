from django import template
from law.models import AlanModel

register = template.Library()

@register.simple_tag
def alanlar_list():
    alanlar = AlanModel.objects.all()
    return alanlar