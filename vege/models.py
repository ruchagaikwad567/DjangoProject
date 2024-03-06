from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    '''user: This is the name of the ForeignKey field in your model.
User: This is the model to which you are creating a foreign key. It is likely the built-in Django User model that is used for authentication.
on_delete=models.CASCADE: This parameter specifies the behavior to adopt when the referenced User object is deleted. In this case, CASCADE means that when the referenced User is deleted, also delete the records in your model that are associated with that User.'''
    receipe_name=models.CharField(max_length=100)
    receipe_description=models.TextField()
    receipe_image=models.ImageField(upload_to='receipe')

