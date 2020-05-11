from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Category')
    
    def __str__(self):
        return self.cat_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='article_pics', blank=True)
    pub_date = models.DateTimeField('date published')
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title