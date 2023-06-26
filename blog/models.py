from django.db import models  #model == table

# Create your models here.
class blog (models.Model):
    title= models.CharField(max_length=250)
    text= models.TextField()
    date= models.DateTimeField()
   
    

    def __str__(self):
        return self.title # without ()
    

class Comment(models.Model):

    post= models.ForeignKey(blog, on_delete=models.CASCADE,related_name="comments")
    name= models.CharField(max_length=50)
    email=models.EmailField()
    content=models.TextField()
    publish=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=True)

    class Meta:
        ordering=("publish",)

    def __str__(self):
        return f"Comment by {self.name}"
    