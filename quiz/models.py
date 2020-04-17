from django.db import models

# Create your models here.
class Questions(models.Model):
    qno = models.IntegerField(unique=True)

    question = models.CharField(max_length=300)

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    ans1 = models.CharField(max_length=20)
    ans2 = models.CharField(max_length=20)
    ans3 = models.CharField(max_length=20)
    ans4 = models.CharField(max_length=20)



