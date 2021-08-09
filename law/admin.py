from django.contrib import admin
from .models import ( NedenBizModeli, SliderModel,IletisimBilgilerModel,
                    IletisimModel,HakkimizdaModel,TimelineModel,AvukatModel,
                    AlanModel,NedenBizModeli,NedenBizImageModel,SoruModel,ReviewModel
  )
# Register your models here.


admin.site.register(SliderModel)
admin.site.register(IletisimBilgilerModel)
admin.site.register(IletisimModel)
admin.site.register(HakkimizdaModel)
admin.site.register(TimelineModel)
admin.site.register(AvukatModel)
admin.site.register(AlanModel)
admin.site.register(NedenBizModeli)
admin.site.register(NedenBizImageModel)
admin.site.register(SoruModel)
admin.site.register(ReviewModel)
