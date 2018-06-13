from django.db import models
import datetime

class Question(models.Model):
    def __str__(self):
        return self.question_text + "->" + self.author_of_question
    def recent_pub(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author_of_question = models.CharField(max_length=100)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)

# Create your models here.
