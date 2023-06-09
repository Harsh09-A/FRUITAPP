from django.contrib import admin
from app.models import Products
from app.models import Addtocart
from app.models import Wishlist
from app.models import Query
# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=('Product_name','Product_Category','Product_Short_Description','Product_Full_Description','Product_Price','Product_Discount_price','Product_Tag','Product_Seo','Product_Unit','Product_img','Product_slide','Product_slide2','created_date',)

@admin.register(Addtocart)
class AddtocartAdmin(admin.ModelAdmin):
    list_display=('Product_id','Product_name','Product_Price','Product_Discount_price','Product_Unit','Product_img','created_date',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display=('Product_id','Product_name','Product_Price','Product_Discount_price','Product_Unit','Product_img','created_date',)

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','city','subject','qmessage','created_date',)

