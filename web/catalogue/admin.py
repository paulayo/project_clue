from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from oscar.core.loading import get_model





ShirtClass = get_model('catalogue', 'ShirtProductClass')
ShirtAttribute = get_model('catalogue', 'ShirtAttribute')
ShirtProduct = get_model('catalogue', 'ShirtProduct')
ShirtOption = get_model('catalogue', 'ShirtOption')
ShirtCategory = get_model('catalogue', 'ShirtCategory')
ShirtRecommendation = get_model('catalogue', 'ShirtRecommendation')



class ShirtAttributeInline(admin.TabularInline):
    model = ShirtAttribute
    extra = 2

# class ShirtRecommendationAdmin(admin.TabularInline):
#     model = ShirtRecommendation
#     fk_name = 'primary'
#     raw_id_fields = ['primary', 'recommendation']
#     pass

class CategoryInline(admin.TabularInline):
    pass


class ShirtAttributeAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'product_class', 'type')
   prepopulated_fields = {"code": ("name", )}
    

class ShirtClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'requires_shipping', 'track_stock')
    inlines = [ShirtAttributeInline]

class ShirtProductAdmin(admin.ModelAdmin):
    pass

class ShirtCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(ShirtCategory)
    list_display = ('name', 'slug')

class ShirtOptionAdmin(admin.ModelAdmin):
    pass

# admin.site.register(ShirtClass, ShirtClassAdmin)
# admin.site.register(ShirtAttribute, ShirtAttributeAdmin)
# admin.site.register(ShirtProduct, ShirtProductAdmin)
# admin.site.register(ShirtOption, ShirtOptionAdmin)
# admin.site.register(ShirtRecommendation, ShirtRecommendationAdmin)
# admin.site.register(ShirtCategory, ShirtCategoryAdmin)

from oscar.apps.catalogue.admin import *