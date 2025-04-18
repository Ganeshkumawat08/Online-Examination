from django.db import models

# Create your models here.

class usermodel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile_number=models.IntegerField(unique=True)
    userid=models.CharField(max_length=20,unique=True,)
    password=models.CharField(max_length=10,unique=True)
    status=models.BooleanField(default=False)
    dob=models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,default='male')
    def __str__(self):
        return self.userid


class subjectmodel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class coursemodel(models.Model):
    name=models.CharField(max_length=100)
    subjects=models.ManyToManyField(subjectmodel)
    def __str__(self):
        return self.name

class papermodel(models.Model):
    subject = models.ForeignKey(subjectmodel, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.IntegerField()  
    def __str__(self):
        return self.question

class resultcoursemodel(models.Model):
    user = models.ForeignKey(usermodel, on_delete=models.CASCADE)
    course=models.CharField(max_length=100)
    subjects=models.CharField(max_length=100)
    marks = models.IntegerField()  
    questions=models.IntegerField() 
    percentage=models.FloatField()
    result=models.CharField(max_length=4)
    def __str__(self):
        return self.course


class resultsubjectmodel(models.Model):
    user = models.ForeignKey(usermodel, on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    questions=models.IntegerField() 
    marks = models.IntegerField()  
    percentage=models.FloatField()
    result=models.CharField(max_length=4)
    def __str__(self):
        return self.subject
