from django.db import models
from django.urls import reverse

# Create your models here.
ReviewTypes = (
  ('E', 'Editorial'),
  ('C', 'Critic'),
  ('A', 'Academic')
)

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
      return self.title

  def get_absolute_url(self):
    return reverse('book-detail', kwargs={'book_id': self.id})

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
    
  
  
