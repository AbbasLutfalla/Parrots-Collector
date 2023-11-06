from django.urls import path
from . import views

urlpatterns =[
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('parrots/', views.parrots_index, name='index'),
path('parrots/<int:parrot_id>', views.parrots_detail, name='detail'),

# Express
# Get the form
# Post the form
path('parrot/create/',views.ParrotCreate.as_view(),name="parrots_create"),
path('parrot/<int:pk>/update/',views.ParrotUpdate.as_view(),name="parrots_update"),
path('parrot/<int:pk>/delete/',views.ParrotDelete.as_view(),name="parrots_delete"),
path('parrot/<int:parrot_id>/add_feeding', views.add_feeding, name='add_feeding'),

# Urls for Toy CRUD Operations
path('toys/', views.ToyList.as_view(), name='toys_index'),
path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'), #Details/Show
path('toys/create/', views.ToyCreate.as_view(), name='toys_create'), 
path('toys/<int:pk>/update', views.ToyUpdate.as_view(), name= 'toys_update'),
path('toys/<int:pk>/delete', views.ToyDelete.as_view(), name= 'toys_delete'),

path('parrots/<int:parrot_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
path('parrots/<int:parrot_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),
]