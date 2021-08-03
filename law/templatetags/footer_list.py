from django import template
from law.models import HakkimizdaModel,AlanModel,IletisimBilgilerModel

register = template.Library()

@register.simple_tag
def footer_list():
    hakkimizda = HakkimizdaModel.objects.first()
    alanlar = AlanModel.objects.all()
    iletisim = IletisimBilgilerModel.objects.first()
    context={
        "hakkimizda":hakkimizda,
        "alanlar":alanlar,
        "iletisim":iletisim,
    }
    return hakkimizda