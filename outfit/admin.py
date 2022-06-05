from django.contrib import admin

from .models import musinsa_model
from .models import mixxo_model
from .models import spao_model

admin.site.register(musinsa_model)
admin.site.register(mixxo_model)
admin.site.register(spao_model)
# Register your models here.
# musinsa_model 을 admin에 보여줌