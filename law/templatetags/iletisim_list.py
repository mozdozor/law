from django import template
from law.models import IletisimBilgilerModel

register = template.Library()

@register.simple_tag
def iletisim_list():
    iletisim = IletisimBilgilerModel.objects.first()
    return iletisim