from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product
)


class CategoeryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('cat_name',)}
    list_display  = ('cat_name','slug')



class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('brand_name',)}
    list_display = ('brand_name','slug')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stocks','created_date','modified_date','is_available')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,CategoeryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand,BrandAdmin)




# Register your models here.
