from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    
    GENDER_CHOICES = [('male', 'Male'),('female', 'Female'),('other', 'Other')]
    COURSE_CHOICES = [('Bsc','Bsc',),('B.com','B.com'),('BA','BA'),('BZC','BZC'),('BBA','BBA')]

    HallTickectnumber = models.CharField(max_length=20)
    Student_name = models.CharField(max_length=50)
    Father_name = models.CharField(max_length=50)
    Mother_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Address = models.TextField()
    Zincode = models.CharField(max_length=10)
    Qualification = models.CharField( max_length=50)
    Yearofpassout=models.CharField( max_length=50)
    Course_duration = models.CharField(max_length=50)
    Enroll_date = models.DateField()
    Course_duration = models.CharField(max_length=50)
    Moblie = models.CharField( max_length=50)
    Emergengynum = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.Student_name

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})
    

class staff1(models.Model):
    name=models.CharField(max_length=50,null=True,blank=False)
    age=models.CharField(max_length=10,null=True,blank=False)
    emailid=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=50,null=True,blank="false")
    Address = models.TextField(null=True,blank=False)
    Position = models.CharField(max_length=50,null=True,blank=False)
    Employment =  models.CharField(max_length=6,null=True,blank=False)
    Dateofjoining = models.TextField(null=True,blank=False)
    Employmentid = models.CharField( max_length=50,null=True,blank=False)
    Highestqualification = models.CharField( max_length=50,null=True,blank=False)
    Institution = models.CharField( max_length=50,null=True,blank=False)
    Yearofgraduation = models.CharField( max_length=50,null=True,blank=False)


class Staff(models.Model):

    EMPLOYMENT_CHOICES = [('full-time', 'FULL-TIME'),('part-time', 'PART-TIME'),('contract', 'CONTRACT'),]
    GENDER_CHOICES = [('male', 'Male'),('female', 'Female'),('other', 'Other'),]

    name=models.CharField(max_length=50,null=True,blank=False)
    age=models.CharField(max_length=10,null=True,blank=False)
    emailid=models.CharField(max_length=100,null=True,blank=False)
    password=models.CharField(max_length=50,null=True,blank="false")
    Address = models.TextField()
    Position = models.CharField(max_length=50)
    Employment =  models.CharField(max_length=6,)
    Dateofjoining = models.TextField()
    Employmentid = models.CharField( max_length=50)
    Highestqualification = models.CharField( max_length=50)
    Institution = models.CharField( max_length=50)
    Yearofgraduation = models.CharField( max_length=50)

    # class Meta:
    #     verbose_name = ("Staff")
    #     verbose_name_plural = ("Staffs")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Staff_detail", kwargs={"pk": self.pk})

class Course(models.Model):
     

     name = models.CharField(max_length=100,null=True,blank=False)
     fathername = models.CharField(max_length=100,null=True,blank=False)
     mothername = models.CharField(max_length=100,null=True,blank=False)
     email = models.EmailField(null=True,blank=False)
     gender = models.CharField(max_length=10,null=True,blank=False)
     specialization = models.CharField(max_length=100,null=True,blank=False)
     name_course = models.CharField(max_length=100,null=True,blank=False)
     coursecode = models.CharField(max_length=10,null=True,blank=False)
     course_duration = models.CharField(max_length=10,null=True,blank=False)

     def __str__(self):
         return self.name