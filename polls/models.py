import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	"""
	This class defines the model Question
	Every question has a question and a publication date
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	
	#admin site view
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?' 

class Choice(models.Model):
	"""
	 Choice has two fields: the text of the choice and a vote tally. 
	 Each Choice is associated with a Question.
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

	

