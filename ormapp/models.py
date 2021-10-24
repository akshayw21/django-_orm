from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    contact=models.CharField(max_length=15)
    college=models.CharField(max_length=50)

class Emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50,primary_key=True)
    contact=models.CharField(max_length=15)
    address=models.TextField(max_length=300)

    class Meta:
        db_table='emp'

    def __str__(self):
        return self.name

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    description=models.TextField(max_length=300)

    class Meta:
        db_table='account'


class Empqualification(models.Model):
    ssc_per=models.IntegerField()
    hsc_per=models.IntegerField()
    gradu_per=models.IntegerField()
    stream=models.CharField(max_length=50)
    emp=models.OneToOneField(Emp,on_delete=models.CASCADE)

    class Meta:
        db_table='emp_qualif'

from django.contrib.auth.models import User
class UserInfo(models.Model):
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class UserInfo2(User):
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    contact=models.CharField(max_length=15)


class Singer(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    email=models.EmailField(max_length=50)

    class Meta:
        db_table='singer'
    
    def __str__(self):
        return self.name

class Songs(models.Model):
    songname=models.CharField(max_length=50)
    duration=models.IntegerField()
    singer=models.ManyToManyField(Singer)

    class Meta:
        db_table='songs'

    def getSingers(self):
        return ','.join([str(i) for i in self.singer.all()])

# python manage.py makemigrations ormapp
# python manage.py migrate ormapp
