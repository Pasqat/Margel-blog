from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Category')
    image = models.ImageField(upload_to='category_pics', blank=True)
    
    def __str__(self):
        return self.cat_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Tag')

    def __str__(self):
        return self.tag_name
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='article_pics', blank=True)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    tag = models.ManyToManyField(Tag)
    pin = models.BooleanField(default=False)

    def __str__(self):
        return self.title

## TODO immagine in categoria
## TODO commenti agli articoli
## TODO pin articoli da tenere in homepgae
## TODO Ricerche articoli per data o parloa chiave