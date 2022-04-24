from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Checkout, cart_update,logout,about,login,bmi, recart,register,contact,gallery,index,pricing,store,equipment,showcart,single,remove,forget,newpass
# from work.models import Login

urlpatterns = [
    path('about/',about,name="about"),
    path('login/',login,name="login"),
    path('register/',register,name='register'),
    path('contact/',contact,name='contact'),
    path('gallery/',gallery,name='gallery'),
    path('',index,name='index'),
    path('pricing/',pricing,name='pricing'),
    path('store/',store,name='store'),
    path('equipment/<str:title>/',equipment),
    path('logout/',logout,name='logout'),
    # path('addcart/<int:id>/',addtocart,name='addtocart'),
    path('showcart/',showcart,name='showcart'),
    path('bmi/',bmi,name='bmi'),
    path('single/<str:title>/',single,name='single'),
    path('remove/<int:id>/',remove,name='remove'),
    path('recart/',recart,name='recart'),
    #  path('forgotpass/',forgot_pass,name = 'forgotpass'),
    # path('otpcheck/',otpcheck, name = 'otpcheck'),
    # path('newpassword/',newpassword, name = 'newpassword'),
    # path("managecart/<int:cp_id>/",ManageCartView, name="managecart")
    path('check/<str:mode>',Checkout,name='check'),
    path('cart_update/<int:id>/',cart_update,name='cart_update'),

    path('forget/',forget,name='forget'),
    path('newpass/',newpass,name='newpass'),
 ]