from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Parrot, Toy
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.views.generic import ListView,DetailView
from .forms import FeedingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ParrotCreate(LoginRequiredMixin, CreateView):
  model = Parrot
  fields ='name', 'breed', 'description','type', 'age', 'image'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ParrotUpdate(LoginRequiredMixin, UpdateView):
  model = Parrot
  fields = ['breed', 'description', 'age']

class ParrotDelete(LoginRequiredMixin, DeleteView):
  model = Parrot
  success_url = '/parrots/'

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')
def parrots_index(request):
  parrots = Parrot.objects.filter(user=request.user)
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
class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy 

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = ['name', 'color']

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

@login_required
def assoc_toy(request, parrot_id,toy_id):
  Parrot.objects.get(id=parrot_id).toys.add(toy_id)
  return redirect('detail', parrot_id=parrot_id)

@login_required
def unassoc_toy(request, parrot_id,toy_id):
  
  Parrot.objects.get(id=parrot_id).toys.remove(toy_id)
  return redirect('detail', parrot_id=parrot_id)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup - Check your details', form.error_messages

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)