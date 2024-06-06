from django.urls import path
from . import views
from myapp.admin import admin_site  # Import the custom admin site
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin_site.urls),  # Use the custom admin site
    path('account', views.account, name='account'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('Error_404', views.Error_404, name='Error_404'),
    path('login/', views.login_view, name='login/'),
    path("Sign_in_FormSubmit/", views.Sign_in_FormSubmit, name='Sign_in_FormSubmit'),
]
