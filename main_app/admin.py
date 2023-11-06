from django.contrib import admin
from .models import Parrot, Feeding, Toy
# Register your models here.

admin.site.register(Parrot)
admin.site.register(Feeding)
admin.site.register(Toy)
