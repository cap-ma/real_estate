from rest_framework import serializers
from .models import Apartment,Banner,Images,UserForm,ApartmentUserForm,MobileImage


class ApartmentLocationSerializer(serializers.Serializer):
    location_lat=serializers.CharField()
    location_long=serializers.CharField()

class MobileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=MobileImage
        fields="__all__"

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields="__all__"

class ApartmentListSerializer(serializers.Serializer):
    images=serializers.SerializerMethodField()
    mobile_images=serializers.SerializerMethodField()

    name=serializers.CharField()
    size_in_m2=serializers.DecimalField(max_digits=9,decimal_places=2)
    room_number=serializers.IntegerField()
    price=serializers.DecimalField(max_digits=15,decimal_places=2)
    description=serializers.CharField()
    location_long=serializers.DecimalField(max_digits=9,decimal_places=6)
    location_lat=serializers.DecimalField(max_digits=9,decimal_places=6)
    address=serializers.CharField()

    def get_images(self,obj):
        main_images=obj.images.filter(main=True).first()
        return ImagesSerializer(main_images).data
    
    def get_mobile_images(self,obj):
        main_images=obj.images.filter(main=True).first()
        return MobileImageSerializer(main_images).data

class ApartmentDetailSerializer(serializers.Serializer):
    images=ImagesSerializer(many=True)
    mobile_images=MobileImageSerializer(many=True)
  
    name=serializers.CharField()
    size_in_m2=serializers.DecimalField(max_digits=9,decimal_places=2)
    room_number=serializers.IntegerField()
    price=serializers.DecimalField(max_digits=15,decimal_places=2)
    description=serializers.CharField()
    location_long=serializers.DecimalField(max_digits=9,decimal_places=6)
    location_lat=serializers.DecimalField(max_digits=9,decimal_places=6)
    address=serializers.CharField()

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields="__all__"

class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserForm
        fields="__all__"

class ApartmentUserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApartmentUserForm
        fields="__all__"

    