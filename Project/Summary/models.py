from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return "Summary of {}".format(self.link)
    
    def get_summary(self):
        return reverse('Summary:Get Summary', kwargs={'id':self.id})

class SummaryNoUser(models.Model):
    link = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return "Summary of {}".format(self.link)
    

class SummaryText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __str__(self):
        return "Summary {} by user {}".format(self.id, self.user.username)
    
    def get_summary(self):
        return reverse('Summary:Get Summary Text', kwargs={'id':self.id})


class SummaryTextNoUser(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return "Summary No. {}".format(self.id)





































