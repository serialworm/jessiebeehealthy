from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category)
    author = models.ForeignKey(Author, default=1)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
