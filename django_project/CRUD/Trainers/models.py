from django.db import models

# Create your models here.
from django.db import models  
class Trainer(models.Model): 
    name = models.CharField(max_length=100)  
    subname = models.CharField(max_length=100)  
    object = models.CharField(max_length=100)  
    class Meta:  
        db_table = "trainer"