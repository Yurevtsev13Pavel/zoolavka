from django.contrib import admin

# Register your models here.
from zoo.models import User, Category,Product, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "phone")
    search_fields = ("name",)
    list_filter = ("name", )
    fields = ('name','phone','number','srok','cvv')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name",)
    list_filter = ("name", )
    fields = ('name','img')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','category')
    search_fields = ("name",)
    list_filter = ("price", )
    fields = ('name','description','price','category','img')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','paid')
    search_fields = ('first_name','last_name')
    list_filter = ("paid", )
    fields = ('first_name','last_name','email','created','updated', 'paid')
    readonly_fields = ("created","updated")

