from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    return os.path.join("media", str(instance.id), filename)

class Blog(models.Model):
	title = models.CharField(max_length=255)
	title_image = models.ImageField(upload_to='media', blank=True, null=True)
	tags = models.ManyToManyField('Tag')
	count_likes = models.AutoField()
	author = models.ForeignKey(User)
	pub_date = models.DateField(auto_now=False, auto_now_add=True)
	mod_date = models.DateField(auto_now=True, auto_now_add=False)
	is_published = models.BooleanField()
	sub_title = model.CharField(max_length=255, blank=True)
	body = models.TextField()
	#content_images = model

	def __str__(self):
        return self.name

class Comments:
	content = models.TextField()
	author = model.CharField(max_length=50, blank=True, null=True)
	parent_blog = model.ForeignKey(Blog, on_delete=models.CASCADE)

	def __str__(self):
        return self.name

class Tags:
	name = model.CharField(max_length=50, blank=False, null=False)

	def __str__(self):
        return self.name

class Media:
	blog = models.ForeignKey(Blog)
	image = models.ImageField(upload_to='media', blank=True, null=True)
	url = model.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
        return self.name


	
	

