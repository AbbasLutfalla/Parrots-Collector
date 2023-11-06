from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Parrot, Toy
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .forms import FeedingForm

class ParrotCreate(CreateView):
  model = Parrot
  fields ='name', 'breed', 'description','type', 'age', 'image'

class ParrotUpdate(UpdateView):
  model = Parrot
  fields = ['breed', 'description', 'age']

class ParrotDelete(DeleteView):
  model = Parrot
  success_url = '/parrots/'

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')
def parrots_index(request):
  parrots = Parrot.objects.all()
  return render(request, 'parrots/index.html', {'parrots': parrots})

def parrots_detail(request, parrot_id):
  parrot = Parrot.objects.get(id=parrot_id)
  feeding_form = FeedingForm()
  toys_parrot_doesnt_have = Toy.objects.exclude(id__in = parrot.toys.all().values_list('id'))
  return render(request, 'parrots/detail.html', {'parrot': parrot, 'feeding_form': feeding_form, 'toys': toys_parrot_doesnt_have})

def add_feeding(request, parrot_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit = False)
    new_feeding.parrot_id = parrot_id
    new_feeding.save()
    return redirect('detail', parrot_id = parrot_id)
  



# CBV' s for Toys CRUD Operation
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy 

class ToyCreate(CreateView):
  model = Toy
  fields = ['name', 'color']

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, parrot_id,toy_id):
  Parrot.objects.get(id=parrot_id).toys.add(toy_id)
  return redirect('detail', parrot_id=parrot_id)

def unassoc_toy(request, parrot_id,toy_id):
  
  Parrot.objects.get(id=parrot_id).toys.remove(toy_id)
  return redirect('detail', parrot_id=parrot_id)
