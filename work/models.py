from django.db import models
from django.db.models.base import Model
choice=[('None','None'),('Muscle Gaining','Muscle Gaining'),('Cardio Fitness','Cardio Fitness'),('Pilates','Pilates'),('Yoga','Yoga'),('Barre','Barre'),('Crossfit','Crossfit')]

class Register(models.Model):
    Firstname=models.CharField(max_length=200)
    Lastname=models.CharField(max_length=200)
    Mobile=models.PositiveIntegerField()
    Exercise=models.CharField(max_length=50,choices=choice,default='None')   
    Age=models.PositiveIntegerField()
    Email=models.EmailField(blank=True)
    Password=models.CharField(max_length=200)
    forgot_ans = models.CharField('Write Something Which Help You To Change Your Password',max_length=100,default='')

    def __str__(self) :
        return self.Firstname


class Review(models.Model):
    message=models.TextField()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()

class Category(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="pro/")
    selling_price=models.PositiveIntegerField()
    description=models.TextField()

    def __str__(self):
        return str(self.title)

class Cart(models.Model):
    orderby=models.ForeignKey(Register,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    subtotal=models.PositiveIntegerField()
    image=models.ImageField(upload_to="pro/")

    def __str__(self):
        return str(self.orderby.Firstname)

class BmiMeasurement(models.Model):
    # user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    height_in_meters = models.FloatField(null=True,blank=True)
    weight_in_kg = models.FloatField(null=True,blank=True)
    measured_at = models.DateField(null=True,blank=True)

    def bmi(self):
        return self.weight_in_kg / self.height_in_meters ** 2