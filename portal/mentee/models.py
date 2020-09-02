from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser

# Create your models here.

class mentee(models.Model):
	mentee_name = models.CharField(max_length=300)
	email = models.EmailField()

	def __str__(self):
		return self.mentee_name

class mentor(models.Model):
	mentor_name = models.CharField(max_length=300)
	email = models.EmailField()
	bio = models.TextField()

	def __str__(self):
		return self.mentor_name

class interview(models.Model):
	# interview_id = 
	mentor = models.ForeignKey(mentor,on_delete=models.CASCADE)
	mentee = models.ForeignKey(mentee,on_delete=models.CASCADE,default=None,blank=True,null=True)
	slot = models.DateTimeField()
	isVacant = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)


class feedback(models.Model):
	
	verdict_choices = [
        ('SH', 'Strong Hire'),
        ('H', 'Hire'),
        ('LH', 'Leaning Hire'),
        ('NH', 'No Hire'),
        ('SNH', 'Strong No Hire')
    ]

	feedback_id = models.ForeignKey(interview,on_delete=models.CASCADE)
	verdict = models.CharField(max_length=20,choices=verdict_choices,default='H')
	# mentee = feedback_id.slot
	rating = models.IntegerField(default=5)
	comments = models.TextField(default='Add Comment',max_length=300)

	def __str__(self):
		return self.verdict



























