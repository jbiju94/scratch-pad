from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    return os.path.join("media", str(instance.id), filename)

class Blog(models.Model):
	title = models.CharField(max_length=255)
	title_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	#tags = models.M
	count_likes = models.AutoField()
	author = models.ForeignKey(User)
	pub_date = models.DateField(auto_now=False, auto_now_add=True)
	mod_date = models.DateField(auto_now=True, auto_now_add=False)
	is_published = models.BooleanField()
	sub_title = model.CharField(max_length=255, blank=True)
	body = models.TextField()
	#content_images = model

class Comments:


class Tags:


class Media:

	

	
	

