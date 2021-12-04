from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('auth/', views.auth, name='auth'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('compare/', views.compare, name='compare'),
    path('contact/', views.contact, name='contact'),
    path('kids/', views.kids, name='kids'),
    path('men/', views.men, name='men'),
    path('merchandising/', views.merchandising, name='merchandising'),
    path('post/', views.post, name='post'),
    path('product/', views.product, name='product'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('women/', views.women, name='women'),
    path('404/', views.page_not_found, name='page_not_found'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('', views.home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
