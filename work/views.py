from ast import Pass
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import BmiMeasurement, Register,Review,Category,Product,Cart
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
# time
import razorpay
from django.views.decorators.csrf import csrf_exempt
import time
from datetime import datetime,timezone
import pytz

import smtplib, ssl
import random
from datetime import date

def about(request):
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'about.html',{'cust':cust})
    else:
        return render(request,'about.html')


def login(request):
    if request.method=="POST":
        try:
            Email=request.POST['Email']
            Password=request.POST['Password']
            mod=Register.objects.get(Email=Email)
            if mod.Password==Password:
                print("if conditions")
                request.session['Email']=Email
                request.session['Firstname']=mod.Firstname
                messages.success(request,'Login Successful')              
            else:
                print("-------------Error-----------------")
                messages.error(request,'Wrong Password')
        except:
            messages.error(request,'User Not Found')
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'login.html',{'cust':cust})
    else:
        return render(request,'login.html')

   
    


def register(request):
    if request.method=="POST":
        Password=request.POST['Password']
        ConfPassword=request.POST['cnfPassword']
        if Password == ConfPassword:
            model=Register()
            model.Firstname=request.POST['Firstname']
            model.Lastname=request.POST['Lastname']
            model.Mobile=request.POST['Mobile']
            model.Age=request.POST['Age']
            model.Exercise=request.POST['Exercise']
            model.Email=request.POST['Email']
            model.Password=request.POST['Password']
            model.forgot_ans=request.POST['fans']
            m=Register.objects.all()
            for a in m:
                if a.Email == model.Email:
                    return render(request,'register.html',{ 'error' : "Email already Existed" })
            model.save()
            # request.session['Email']=model.Email
            return redirect("login")
        else:
            return render(request,'register.html',{ 'msg' : "Plz Enter Pame Password" })
    # return render(request,'register.html')
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'register.html',{'cust':cust})
    else:
        return render(request,'register.html')

def contact(request):
    if request.method=="POST":
        model=Review()
        model.message=request.POST['message']
        model.name=request.POST['name']
        model.email=request.POST['email']
        model.mobile=request.POST['mobile']
        model.save()
        return redirect("contact")
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'contact.html',{'cust':cust})
    else:
        return render(request,'contact.html')
    


def gallery(request):
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'gallery.html',{'cust':cust})
    else:
        return render(request,'gallery.html')
   

def index(request):
    try:
        q=request.GET.get('search')
        print(q)
    except:
        q=None
    if q:
        x=Product.objects.filter(Q(title__icontains=q))  
      
        data={
            'pro': x,
             }
    else:
        data={}
        print('no')
    return render(request,'index.html',data)
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'index.html',{'cust':cust})
    else:
        return render(request,'index.html')
    

def pricing(request):
    if request.session.get('Email'):
        cust=Register.objects.get(Email=request.session['Email'])
        return render(request,'pricing.html',{'cust':cust})
    else:
        return render(request,'pricing.html')
    

def store(request):
    if 'Email' in request.session:
        mod=Product.objects.all()
        f=Category.objects.all()
        return render(request,'store.html',{'mod':mod ,'f':f})
    else:
        mod=Product.objects.all()
        f=Category.objects.all()
        return render(request,'store.html',{'mod':mod ,'f':f}) 
        
    #  if request.session.get('Email'):
    #     cust=Register.objects.get(Email=request.session['Email'])
    #     return render(request,'pricing.html',{'cust':cust})
    #  else:
    #     return render(request,'pricing.html')




def equipment(request,title):
    f1=Category.objects.get(title=title)
    if f1.title=='Powder':
        pro=Product.objects.filter(category=f1)
        return render(request,'equipment.html',{'pro':pro})
    else:
        prod=Product.objects.filter(category=f1)
        return render(request,'powder.html',{'prod':prod})

def logout(request):
    if 'Email' in request.session:
        del request.session['Email']
        return redirect('login')
    else:
        return redirect('login')




def showcart(request):
    if 'Email' in request.session:
        tot=0
        email=Register.objects.get(Email=request.session['Email'])
        show_data=Cart.objects.all().filter(orderby=email)
        for i in show_data:
            tot+=i.subtotal
        request.session['Order_total']=tot
        razorpay_amount=tot*100
        if request.method == "POST":
            amount = razorpay_amount
            client = razorpay.Client(
                auth=("rzp_test_bgP5kN1nzFNjoS", "HAf1PmDUxTZwLeDPBscspNtM"))

            payment = client.order.create({'amount': amount, 'currency': 'INR',
                                        'payment_capture': '1'})
            show_data.delete()
        return render(request,'cart.html',{'data':show_data,'total':tot,'email':email,'razor':razorpay_amount})
    else:
        return redirect('login')

def single(request,title):
    if 'Email' in request.session:
        pro=Product.objects.get(title=title)
        return render(request,'single.html',{'pro': pro})
    else:
        prod=Product.objects.get(title=title)
        return render(request,'single.html',{'pro': prod})

def remove(request,id):
    remcart=Cart.objects.get(id=id)
    remcart.delete()
    return redirect('showcart')

def recart(request):
    rcart=Cart.objects.all()
    rcart.delete()
    return redirect('showcart')


def Checkout(request,mode):
    tz= pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(timezone.utc).astimezone(tz)
    millis = int(time.mktime(time_now.timetuple()))
    order_id = "Order"+str(millis)
    request.session['Order_id'] = order_id
    return redirect('showcart')

def cart_update(request,id):
    if 'Email' in request.session:
        user=Register.objects.get(Email=request.session['Email'])
        print(user)
        product_id = Product.objects.get(id=id)
        print(product_id)
        try:
            item=Cart.objects.get(product=product_id)
            item.quantity+=1
            item.subtotal=product_id.selling_price+item.subtotal
            item.save()
            print(item)
        except Cart.DoesNotExist:
            new=Cart.objects.create(orderby=user,product=product_id,quantity=1,subtotal=product_id.selling_price,image=product_id.image)
            new.save()
            print('Done')
        return redirect('showcart')
    else:
        return redirect('login')

def forget(request):
    print("Inside forget pass function")
    if request.POST:
        data = request.POST['conf']
        try:
            valid = Register.objects.get(forgot_ans=data)
            print(valid,'*********************************')
            if valid:
                request.session['user'] = valid.Email
                return redirect('newpass')
            else:
                return render(request,'forget.html',{ 'msg' : "Wrong Answer" })    
        except:
            return render(request,'forget.html',{ 'msg' : "Wrong Answer" })
    return render(request, "forget.html")

def newpass(request):
    print("Inside new pass function")
    if 'user' in request.session:
        print(request.session['user'])
        if request.POST:
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            if pass1 == pass2:
                print("Password matched")
                obj = Register.objects.get(Email=request.session['user'])
                obj.Password = pass2
                obj.save()
                del request.session['user']
                print("changed successfully")
                return redirect('login')
            else:
                return render(request,'newpass.html',{ 'msg' : "Please Enter Same Password" })
        return render(request,'newpass.html')
    return redirect('logi')

    
# def home(request):
#     if 'Email' in request.session:
#         user=Register.objects.get(Email=request.session['Email'])
#         if request.method == "POST":
#             name = request.POST.get('name')
#             amount = 50000

#             client = razorpay.Client(
#                 auth=("rzp_test_bgP5kN1nzFNjoS", "HAf1PmDUxTZwLeDPBscspNtM"))

#             payment = client.order.create({'amount': amount, 'currency': 'INR',
#                                         'payment_capture': '1'})
#         return render(request, 'index.html')
#     else:
#         return redirect('login')

@csrf_exempt
def success(request):
    return render(request, "success.html")

def bmi(request):
    bmi=0.00
    if request.method == "POST":
        model=BmiMeasurement()
        model.height_in_meters=request.POST['height_in_meters']
        model.weight_in_kg=request.POST['weight_in_kg']
        model.measured_at=date.today()
        model.save()
        bmi = float(float(model.weight_in_kg)/float(model.height_in_meters))*2
        print(bmi)
        redirect('bmi')
    return render(request, "bmi.html", {"bmi": bmi})
    # return render(request, "bmi.html", {"form": form})