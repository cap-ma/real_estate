from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import MainImages

class Apartment(models.Model): 

    Status=(
        (("on sale"),_("on sale")),
        (("unavailable"),_("unavailable")),
    )

    name=models.CharField(_("name"),max_length=128)
    size_in_m2=models.DecimalField(_("size"),max_digits=9,decimal_places=2)
    room_number=models.IntegerField(_("room_number"))
    price=models.DecimalField(_("price"),max_digits=15,decimal_places=2)
    description=models.TextField(_("description"))
    location_lat=models.DecimalField(_("latitude"),max_digits=9, decimal_places=6)
    location_long=models.DecimalField(_("longtitude"),max_digits=9,decimal_places=6)
    address=models.CharField(_("address"),max_length=128)
    status=models.CharField(_("status"),max_length=15,choices=Status,default=Status[0])

    class Meta:
        verbose_name=_("apartment")
        verbose_name_plural=_("apartments")

    def __str__(self) -> str:
        return self.name
    
class MobileImage(models.Model):
    file=models.ImageField(_("file"),upload_to='media/apartments')
    main=models.BooleanField(_("main"),default=False)
    apartment=models.ForeignKey(Apartment,on_delete=models.DO_NOTHING,related_name='mobile_images')

    def __str__(self) -> str:
        return f"{self.main} and {self.apartment}"

class Images(models.Model):
    file=models.ImageField(_("file"),upload_to='media/apartments')
    main=models.BooleanField(_("main"),default=False)
    apartment=models.ForeignKey(Apartment,on_delete=models.DO_NOTHING,related_name='images')

    def __str__(self) -> str:
        return f"{self.main} and {self.apartment}"

    objects=models.Manager()
    main_images=MainImages()

    class Meta:
        verbose_name=_("image")
        verbose_name_plural=_("images")

class Banner(models.Model):
    image=models.ImageField(_("image"),upload_to="media/banner")

    def __str__(self) -> str:
        return self.image.path
    
    
    class Meta:
        verbose_name=_("banner")
        verbose_name_plural=_('banners')

class UserForm(models.Model):
    STATUS_CHOICES = (
        ('new', _('new')),
        ('connected', _('connected')),
        ('pending', _('Pending')),
    )
        
    name=models.CharField(_("name"),max_length=128)
    phone_number=models.CharField(_("phone_number"),max_length=14)
    message=models.TextField(_("message"))
    status = models.CharField(_("status"),max_length=10, choices=STATUS_CHOICES,default=STATUS_CHOICES[0])

    def __str__(self) -> str:
        return self.phone_number
    
    class Meta:
        verbose_name=_("user form")
        verbose_name_plural=_('user forms')

class ApartmentUserForm(models.Model):

    STATUS_CHOICES = (
        ('new', _('new')),
        ('connected', _('connected')),
        ('pending', _('Pending')),
    )


    name=models.CharField(_("name"),max_length=128)
    phone_number=models.CharField(_("phone_number"),max_length=14)
    message=models.TextField(_("message"))
    apartment=models.ForeignKey(Apartment,on_delete=models.DO_NOTHING,related_name=_("apartment"))
    status = models.CharField(_("status"),max_length=10, choices=STATUS_CHOICES,default=STATUS_CHOICES[0])


    def __str__(self) -> str:
        return self.phone_number
    
    class Meta:
        verbose_name=_("apartment user form")
        verbose_name_plural=_("apartment user forms")



