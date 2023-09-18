from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminSubscribe(admin.ModelAdmin):
    list_display = ['id','ism','fam','username','tg_id']
admin.site.register(Subscribe,AdminSubscribe)

class AdminMenu_uz(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu_uz,AdminMenu_uz)

class AdminMenu_ru(admin.ModelAdmin):
    list_display = ['id','nomi']
admin.site.register(Menu_ru,AdminMenu_ru)

class AdminTest_savollar(admin.ModelAdmin):
    list_display = ['id','savol','variant1','variant2','variant3','variant4','tur']
admin.site.register(Test_savollar,AdminTest_savollar)

class AdminTest_savollarru(admin.ModelAdmin):
    list_display = ['id','savol','variant1','variant2','variant3','variant4','turru']
admin.site.register(Test_savollarru,AdminTest_savollarru)

class AdminNatijalar(admin.ModelAdmin):
    list_display = ['id','savol_id','savol','javob','tg_id','tur','status']
admin.site.register(Natijalar,AdminNatijalar)

class AdminNatijalarru(admin.ModelAdmin):
    list_display = ['id','savol_id','savol','javob','tg_id','turru','status']
admin.site.register(Natijalarru,AdminNatijalarru)