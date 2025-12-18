from django.contrib import admin
from .models import Mammal, Bird

# Register your models here.
admin.site.register(Mammal)
admin.site.register(Bird)