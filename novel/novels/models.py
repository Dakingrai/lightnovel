from django.db import models
STATUS = (
        ('ONGOING', "Ongoing"),
        ('COMPLETED', "Completed"),
    )
# Create your models here.
class Novel(models.Model):

    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/images')
    description = models.TextField(null=True)
    genre = models.ManyToManyField('Genre', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length= 40, choices=STATUS)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    chapter = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=500, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

