from django.db import models
STATUS = (
        ('ONGOING', "Ongoing"),
        ('COMPLETED', "Completed"),
    )

FEATURED = (
    (0, 'No'),
    (1, 'Everywhere'),
    (2, 'Front Page')
)
# Create your models here.
class Novel(models.Model):

    name = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/images')
    description = models.TextField(null=True)
    genre = models.ManyToManyField('Genre', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length= 40, choices=STATUS)
    featured = models.IntegerField(choices= FEATURED, default=0)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    class Meta:
        db_table = "novels_chapter"
        managed = False

    id = models.AutoField(primary_key=True, null=False)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    chapter = models.IntegerField(null=False)
    chapter_content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=500, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

