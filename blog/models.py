from django.db import models
# Create your models here.


class Blogs(models.Model):
    objects = models.Manager()
    image_url = models.CharField(max_length=2080)
    title = models.CharField(max_length=255, unique=True)
    summary = models.CharField(max_length=255, null=True)
    body = models.TextField()
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('blog.Category', on_delete=models.CASCADE)


class Category(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
