from django.contrib import admin
from .models import Images,Banner,Apartment,UserForm,ApartmentUserForm

admin.site.register(Images)
admin.site.register(Banner)
admin.site.register(Apartment)
admin.site.register(UserForm)
admin.site.register(ApartmentUserForm)

