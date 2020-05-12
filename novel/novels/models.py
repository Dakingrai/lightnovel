from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

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

    def get_absolute_url(self):
        slug = slugify(f"{self.name}")
        return reverse("novel", kwargs={"id": self.id, "slug": slug})


class Chapter(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=1000)
    chapter = models.IntegerField(null=False)
    chapter_content = models.TextField(null=True)

    slug = models.SlugField(unique=True, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.novel.name}")
        super(Chapter, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("chapter", kwargs={"slug": self.slug, "chapter":self.chapter})

class Genre(models.Model):
    name = models.CharField(max_length=500, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

