
from django.db import models

# Create your models here.

class alumni_tb(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  team_name = models.CharField(max_length=255)
  points_scored = models.IntegerField()

def __str__(self):
     return f"{self.first_name} {self.last_name}  { self.team_name } { self.points_scored }"

  
# THIS IS THE ALUMNI CENTER TABLE
class dzolali(models.Model):
  Item_Name = models.CharField(max_length=255)
  Brand_Name = models.CharField(max_length=255)
  Quantity = models.IntegerField()
  Remark = models.TextField()

def __str__(self):
     return f"{self.Item_Name} {self.Brand_Name}  { self.Quantity } { self.Remark }"   


# THIS IS THE LEASED TABLE
class leased(models.Model):
  Item_Name = models.CharField(max_length=255)
  Brand_Name = models.CharField(max_length=255)
  Recipient = models.CharField(max_length=255)
  Department = models.CharField(max_length=255)
  Quantity = models.IntegerField()
  Receive_Date = models.DateField()
  Return_Date = models.DateField()
  Remark = models.TextField()

def __str__(self):
     return f"{self.Item_Name} {self.Brand_Name}  { self.Recipient }  { self.Department }   { self.Quantity } { self.Receive_Date } { self.Return_Date } { self.Remark }"   

# THIS IS THE BOOK TABLE
class books(models.Model):
  Title = models.CharField(max_length=255)
  Author = models.CharField(max_length=255)
  Quantity = models.IntegerField()
  Remark = models.TextField()

def __str__(self):
     return f"{self.Title} {self.Author}  { self.Quantity } { self.Remark }" 