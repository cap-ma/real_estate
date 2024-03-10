from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from django.core.cache import cache 
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from .models import Apartment,Banner,UserForm,ApartmentUserForm
from .serializers import ApartmentListSerializer,ApartmentDetailSerializer,BannerSerializer,\
    UserFormSerializer,ApartmentUserFormSerializer
from rest_framework.response import Response
import time

def log_db_queries ( f ) :
    from django.db import connection
    def new_f ( * args , ** kwargs ) :
        start_time = time.time()
        res = f ( * args , ** kwargs )
        print ( "\n\n" )
        print ( "-"*80 )
        print ("db queries log for %s:\n" % (f.__name__))
        print ( " TOTAL COUNT : % s " % len ( connection.queries ) )
        for q in connection.queries :
            print ("%s: %s\n" % (q["time"] , q["sql"]))
        end_time = time.time ()
        duration = end_time - start_time
        print ('\n Total time: {:.3f} ms'.format(duration * 1000.0))
        print ("-"*80)
        return res
    return new_f

class ApartmentListView(ListAPIView):
    queryset=Apartment.objects.all()
    serializer_class=ApartmentListSerializer
    
    @swagger_auto_schema(tags=['Landing'])
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)

class ApartmentDetailView(RetrieveAPIView):
    queryset=Apartment.objects.all()
    serializer_class=ApartmentDetailSerializer
    lookup_field='pk'
    
class BannerListView(ListAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer

    # @swagger_auto_schema(tags=['Landing'])
    # @log_db_queries
    # def get(self,request,*args,**kwargs):
    #     print('this is cache-----',cache)
    #     if "banners" in cache:
    #         data=cache.get('banners')
    #         return Response(data)
    #     else:
    #         queryset=Banner.objects.all()
    #         serializer_class=BannerSerializer(queryset,many=True)
    #         cache.set("banners",serializer_class.data,timeout=30)
    #         return super().get(request,*args,**kwargs)
        
    
class UserFormCreateView(CreateAPIView):
    queryset=UserForm.objects.all()
    serializer_class=UserFormSerializer

class AparetmentUserFormCreateView(CreateAPIView):
    queryset=Apartment.objects.all()
    serializer_class=ApartmentUserFormSerializer



    
    

