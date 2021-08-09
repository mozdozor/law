
from law.models import IletisimModel
from django import template



register=template.Library()




@register.simple_tag
def messageExistAdmin():
    emails=IletisimModel.objects.filter(okundu_mu="no")
    return emails





# @register.simple_tag
# def addTwoNumber():
#     emails=IletisimModel.objects.filter(okundu_bilgisi="okunmadı")
#     yazilar=YaziModel.objects.filter(is_published="no")
#     return emails.count()+yazilar.count()