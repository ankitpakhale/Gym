from django.contrib import admin
from .models import Category, Product, Register,Review,Cart,BmiMeasurement


admin.site.register([Register,Review,Category,Product,Cart,BmiMeasurement])



