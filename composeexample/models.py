from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField

class College(models.Model):
    id = models.IntegerField(primary_key=True)
    #Use default id maybe?
    name = models.CharField(max_length=30)
    def __str__ (self):
        return self.name

class Fields(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    pid = models.IntegerField() #program id; how long?
    college = models.ForeignKey(College,on_delete=models.CASCADE)   
    def __str__ (self):
        return self.name

class IProgram(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    pid = models.IntegerField() #program id; how long?
    field = models.ForeignKey(Fields,on_delete=models.CASCADE)
    def __str__ (self):
        return self.name

    
class Classes(models.Model):
    id = models.IntegerField(primary_key=False)
    name = models.CharField(max_length=30)
    cid = models.CharField(max_length=20,primary_key=True) 
    Description = models.CharField(max_length=100)
    field = models.ForeignKey(Fields,on_delete=models.CASCADE)
    def __str__ (self):
        return self.name

class Quarter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    startdate = models.DateField()
    enddate = models.DateField()
    def __str__ (self):
        return self.name

class ClassesQ(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Classes,on_delete=models.CASCADE)
    quarter = models.ForeignKey(Quarter,on_delete=models.CASCADE)
    def __str__ (self):
        return self.cid

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    pid = models.ForeignKey(IProgram,on_delete=models.CASCADE)
    #might need a null program as deafult
    classes = JSONField()
    #since a student might have lots of transcripts
    def __str__ (self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class Files(models.Model):
    file = models.FileField()
    def __str__(self):
        return self.file.name