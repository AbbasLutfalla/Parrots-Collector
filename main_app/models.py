from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

# Tuple
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})



class Parrot(models.Model):
  name = models.CharField(max_length=100) # max field
  breed = models.CharField(max_length=100) # max field
  description = models.TextField(max_length=250) # Text Are
  type = models.TextField(max_length=50)
  age = models.IntegerField() # Int field
  image = models.ImageField(upload_to='main_app/static/uploads', default='')
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse('detail', kwargs={'parrot_id': self.id})
  
  def __str__(self):
    return f"{self.name}"
  
def fed_for_today(self):
  return self.feeding_set.filter(date=date.today()).count >= len(MEALS)
    
class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(max_length=1, 
                          choices=MEALS, default=MEALS[0][0])
  parrot = models.ForeignKey(Parrot, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.parrot.name}{self.get_meal_display()} on {self.date}"

class Meta:
  ordering = ['-date']