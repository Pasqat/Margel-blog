from django.db import models
from django.utils import timezone
from django.urls import reverse

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
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='article_pics', blank=True)
    pub_date = models.DateTimeField('date published', blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    tag = models.ManyToManyField(Tag)
    pin = models.BooleanField(default=False)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog_app:article_detail", kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog_app:article_list')

    def __str__(self):
        return self.text


## TODO Ricerche articoli per data o parloa chiave