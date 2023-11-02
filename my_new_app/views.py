from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Parrot:
  def __init__(self, name, breed, type, description, age):
    self.name = name
    self.breed = breed
    self.type = type
    self.description =description
    self.age = age

parrots = [
  Parrot('Bebo', 'Tabby', 'casco','Gray Birds ', 21),
  Parrot('tomahawk', 'Egs','Macaw', 'Blue Birds ', 4),
  Parrot('ango', 'Young','Bald eagle', 'white heads and tails with dark brown bodies  ', 1),
]
def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def parrots_index(request):
  return render(request, 'parrots/index.html', {'parrots': parrots})