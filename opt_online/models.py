from django.db import models

# Create your models here.



class Goods(models.Model):
	code = models.CharField(max_length=30, unique=True)
	articul = models.CharField(max_length=30)
	producer = models.CharField(max_length=50)
	description = models.TextField()
	category = models.ForeignKey('Category', null=True, blank=True)
	price = models.FloatField()	
	photo = models.CharField(max_length=100, blank=True, null=True)

	def path_photo(self, path):
		self.photo = path
		return 'Путь фото: {} для товара {}'.format(self.path, self.code)


	def __str__(self):
		return "Code {} and Articul {} and Producer".format(self.code, self.articul, self.producer)


	def save(self, *args, **kwargs):
		super(Goods, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		super(Goods, self).delete(*args, **kwargs)

	class Meta:
		unique_together = ('code', 'articul', 'producer')

class Category(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()

	def __str__(self):
		return self.name