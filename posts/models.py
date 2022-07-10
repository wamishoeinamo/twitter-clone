
from django.db import models
from cloudinary.models import CloudinaryField


class Post(models.Model):
    class meta(object):
        db_table = 'posts'

    name = models.CharField(
            'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
     )
    body = models.CharField(
    'Body', blank=True, null=True,max_length=140, db_index=True
    )
    image = CloudinaryField( 
        'image', blank=True, db_index=True
    )
    created_at= models.DateTimeField(
    'Created DateTime', blank=True, auto_now_add=True
    )
    likes = models.PositiveBigIntegerField(
        'like', default=0, blank=True, db_index=True
    )
