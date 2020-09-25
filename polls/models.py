from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	question_text = models.CharField(max_length=200)
	create_date = models.DateTimeField(default=timezone.now)
	pub_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.pub_date = timezone.now()
		self.save()

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text