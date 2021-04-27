from django.contrib import admin



# Register your models here.
from .models import Brand , Category , Product
from .models import CartItem


admin.site.register(CartItem)
admin.site.register(Brand)
admin.site.register(Category)




class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag","name","price","brand","category"]
    search_fields = ["name","brand__name"]
    list_filter = ["brand","category"]

admin.site.register(Product , ProductAdmin)

