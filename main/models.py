"""
Main Models
Developed By : Erum Mehmood & Khalid Awan

"""
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image


# Create your models here.

class Countries(models.Model):
	country_id = models.AutoField(primary_key=True)
	country = models.CharField(max_length=50, null=True)
	country_code = models.CharField(max_length=2, null=True)
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Countries"
	
	def __str__(self):
		return f'{self.country}'

class States(models.Model):
	state_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(Countries, default = 1, on_delete=models.CASCADE)
	state_code = models.CharField(max_length=4, null=True)
	state = models.CharField(max_length=50, null=True)#state name
	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "States"
	
	def __str__(self):
		return f'{self.state}'

class Cities(models.Model):
	city_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(Countries, default = 1, on_delete=models.CASCADE)
	state = models.ForeignKey(States, default = 1, on_delete=models.CASCADE)
	city_code = models.CharField(max_length=4, null=True)
	city = models.CharField(max_length=50, null=True)# city name
	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Cities"
	
	def __str__(self):
		return f'{self.city}'

#class EndUser(models.Model):
#	user_id = models.IntegerField(primary_key=True)
#	#country = models.IntegerField(default = 0)
#	country = models.ForeignKey(Countries, default = 1, on_delete=models.CASCADE)
#	first_name = models.CharField(max_length=100)
#	last_name = models.CharField(max_length=100)
#	email = models.CharField(max_length=100, blank = True) # write email validator
#	username = models.CharField(max_length=100, unique=True)
#	last_login = models.CharField(max_length=100, blank = True)
#	is_active = models.CharField(max_length=100, blank = True)
#	date_joined = models.DateTimeField(auto_now = True, blank = True)
#	photo = models.ImageField(default='default.png',upload_to='user_photos' , blank = True)
#	mobile = models.CharField(max_length=10,null=True, blank = True)
#	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
#	address = models.TextField(blank=True)
#	pincode = models.CharField(max_length=6, null=True, blank=True)
#	locality = models.CharField(max_length=100, null=True, blank=True)
#	city = models.CharField(max_length=100, null=True, blank=True)
#	state = models.CharField(max_length=50, null=True, blank=True)
	
#	def __str__(self):
#		return f'{self.user_id}'
	
#	'''	
#	def save(self, *args, **kwargs):

#		img = Image.open(self.photo.path)
#		if img.height > 300 or img.width > 300:
#			output_size = (300, 300)
#			img.thumbnail(output_size)
#			img.save(self.photo.path)
#	'''

#class FinancialDetail(models.Model):
#	user = models.OneToOneField(EndUser, on_delete=models.CASCADE,primary_key=True)	
#	f_id = models.IntegerField() # financial id
#	country = models.ForeignKey(Countries, on_delete=models.CASCADE)
#	bank_name = models.CharField(max_length=50, null=True , blank=True)# write validator
#	account_name = models.CharField(max_length=50, null=True, blank=True)# write validator
#	account_no = models.CharField(max_length=50, null=True, blank=True)# write validator
#	branch_no = models.CharField(max_length=50, null=True, blank=True)# write validator
#	class Meta:
#		unique_together = (('user', 'f_id'),)# user_id, f_id
