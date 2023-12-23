from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    image = models.ImageField(
        upload_to='images/', default='../default_profile_tl2tw0'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, )
    status = models.CharField(choices=options, max_length=10, default='published')
    postobjects = PostObjects()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

