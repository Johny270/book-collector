from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
ReviewTypes = (
  ('E', 'Editorial'),
  ('C', 'Critic'),
  ('A', 'Academic')
)
class Cover(models.Model):
  cover_type = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.cover_type
  
  def get_absolute_url(self):
    return reverse('cover-detail', kwargs={'pk': self.id})

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  covers = models.ManyToManyField(Cover)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse('book-detail', kwargs={'book_id': self.id})

  def review_for_today(self):
    return self.review_set.filter(date=date.today()).count() >= len(ReviewTypes)

class Review(models.Model):
  date = models.DateField()
  review_type = models.CharField(
    max_length=1,
    choices=ReviewTypes,
    default=ReviewTypes[0][0]
  )
  body = models.TextField(max_length=500)

  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_review_type_display()} on {self.date}"

  class Meta:
    ordering = ['-date']



    
  
    
  
  
