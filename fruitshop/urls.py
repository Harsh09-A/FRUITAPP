from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    # ..................pages......................
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('shop/', views.shop, name="shop"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('wishlist/', views.wishlist, name="wishlist"),
    path('myacc/', views.myacc, name="myacc"),
    # ...................end pages..............................
    # ...................start database querys.........................
    path('query/', views.query, name="query"),
    path('regdata/', views.regdata, name="regdata"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('logout/', views.logout, name="logout"),
    path('product/<int:id>', views.product, name="product"),
    path('addcard/<int:id>', views.addcard, name="addcard"),
    path('whishlist2/<int:id>', views.whishlist2, name="whishlist2"),
    path('adddel/<int:id>', views.adddel, name="adddel"),
    path('wishdel/<int:id>', views.wishdel, name="wishdel"),
    # .......................................................

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)