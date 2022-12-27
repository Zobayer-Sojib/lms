from django.db import models

# Create your models here.
class book(models.Model):
    book_name = models.CharField(max_length=50)
    book_writer = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    book_id = models.IntegerField()

 

    def __str__(self):
        return self.book_name



class BookDB(models.Model):
    Title = models.CharField(max_length=200)
    Book_Details = models.CharField(max_length=1100)
    Available = models.IntegerField()


    def __str__(self):
        return self.Title