from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
		  (0, "Draft"),
		  (1, "Published")
)

class Post(models.Model):
	title=models.CharField(max_length=200, unique=True)
	slug=models.SlugField(max_length=200, unique=True)
	author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
	content=models.TextField()
	excerpt=models.TextField(blank=True)
	"""
	In the case of a ForeignKey being used multiple times,
	we must specify the related_name property to make it 
	distinct from the "author" property.
	"""
	participants=models.ManyToManyField(User, related_name="participants", blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)
	status=models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering=['-updated_on','-created_on']

	def __str__(self):
		return f"{self.title} | {self.author}"
	

class Comment(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
	content=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	approved=models.BooleanField(default=False)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return f"{self.author} on: {self.post}"