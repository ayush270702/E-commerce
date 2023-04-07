from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_title = "SaleSwipe"
admin.site.site_header = "SaleSwipe"
admin.site.index_title = "Abc Buy"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','description')
    search_fields = ('name',)
    
    def discount_20(self,request,queryset):
        for q in queryset:
            f = (q.price)-(q.price*0.2)
            queryset.update(price = f)
    
    actions = ('discount_20',)
    
    list_editable = ('price','description')
    
    

admin.site.register(Product, ProductAdmin)