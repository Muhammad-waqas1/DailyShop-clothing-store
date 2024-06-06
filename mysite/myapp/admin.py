from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import MyModel
from django.contrib.auth.models import User, Group

# Register your models here.
from .models import User

admin.site.register(User)



class MyAdminSite(AdminSite):
    site_header = 'Daily Shop | Clothing Store'
    site_title = 'Daily Shop - Clothing Store'
    index_title = 'Welcome to My Daily Shop Panel'

admin_site = MyAdminSite(name='Rashid')

# Unregister the default User and Group models from the custom admin site
admin_site.register(User)
admin_site.register(Group)
admin_site.register(MyModel)