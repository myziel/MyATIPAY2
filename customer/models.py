"""
Customer Models
Developed By : Erum Mehmood & Khalid Awan

"""


from django.db import models
from main.models import Countries, States, Cities
from PIL import Image
from mptt.models import MPTTModel, TreeForeignKey
from datetime import date, datetime





class Customer(models.Model):
	customer_id = models.AutoField(primary_key=True)
	upliner = models.IntegerField(blank=False)
	ref_id = models.IntegerField(blank=False)
	RIGHT = 'Right'
	LEFT = 'Left'
	POSITION_CHOICES = [
        (RIGHT, 'Right'),
        (LEFT, 'Left'),
    ]
	position = models.CharField(
        max_length=5,
        choices=POSITION_CHOICES,
        default=RIGHT,
    )
	
	username = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	#country = models.IntegerField(default = 0)
	
	
	def __str__(self):
		return f'ID: {self.customer_id}, Username: {self.username}'

	def get_all_objects(self):
		queryset = self._meta.model.objects.all()
		return queryset

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Customer"


class CustomerDetail(models.Model):
	#customer = models.OneToOneField(Customer,default =0,  on_delete=models.CASCADE,primary_key=True)
	customer_id = models.AutoField(primary_key=True)
	country = models.ForeignKey(Countries, default =167,on_delete=models.CASCADE)
	state = models.ForeignKey(States, default =1,on_delete=models.CASCADE)
	city = models.ForeignKey(Cities, default =86,on_delete=models.CASCADE)
	#country = models.CharField(max_length=50, blank = True)
	#state = models.CharField(max_length=50, blank = True)
	#city = models.CharField(max_length=50, blank = True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, blank = True) # write email validator
	last_login = models.CharField(max_length=100, blank = True)
	is_active = models.CharField(max_length=100, blank = True)
	date_joined = models.DateTimeField(auto_now = True, blank = True)
	photo = models.ImageField(default='images/face.jpg',upload_to='user_photos/' , blank = True)
	mobile = models.CharField(max_length=10,null=True, blank = True)
	alternate_mobile = models.CharField(max_length=10,null=True,blank=True)
	address = models.TextField(blank=True)
	zipcode = models.CharField(max_length=6, null=True, blank=True)
	GENDER_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	gender = models.CharField(max_length=6,choices=GENDER_CHOICES, null=True, blank = True)	
	dob = models.DateField(null = True, blank = True)
	cnic = models.CharField(max_length=50, null=True, blank = True)# write cnic validator
	cp_points = models.FloatField(null=True, blank=True, default=0.0)
	t_personal_earning = models.FloatField(null=True, blank=True, default=0.0)
	withdrawel_amount = models.FloatField(null=True, blank=True, default=0.0)
	ewallet = models.FloatField(null=True, blank=True, default=0.0)
	BLACKLIST = 'Blacklist'
	SUSPEND = 'Suspend'
	ACTIVE = 'Active'
	INACTIVE = 'InActive'
	STATUS_CHOICES = [
        (BLACKLIST , 'Blacklist'),
        (SUSPEND , 'Suspend'),
		(ACTIVE , 'Active'),
		(INACTIVE , 'InActive'),
    ]
	status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE,
    )

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

	def __str__(self):
		return f'Name: {self.first_name} {self.last_name}'

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Customer Detail"

class CustomerLogin(models.Model):
	login_id = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # customer id
	ip = models.CharField(max_length=50, null=True, blank = True) # customer ip
	login_date = models.DateField(blank = True, default = date.today())
	login_time = models.TimeField(blank = True, default = datetime.now())
	wrong_login_attempt = models.IntegerField(default = 0)
	today_login_attempt = models.IntegerField(default = 0)
	is_now_login = models.BooleanField(default=False)
	

	class Meta:
		# Gives the proper plural name for admin
		verbose_name_plural = "Customer Login"
	

# model test
#class Tag(models.Model):
#    name = models.CharField(max_length=50)
#    description = models.CharField(max_length=100, blank=True)
#    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

#    # Not necessary, can use Tag.tag_set.all()
#    # But this function uses pk which allows
#    #    rootTag=Tag() 
#    #    rootTag.children()
#    # Because rootTag has no pk
#	#def __str__(self):
#	#	return f'Name: {self.name}'

#    def children(self):
#        return Tag.objects.filter(parent=self.pk)

#    def serializable_object(self):
#        obj = {'name': self.name, 'children': []}
#        for child in self.children():
#            obj['children'].append(child.serializable_object())
#        return obj


## test model
#class Catalog(MPTTModel):
#	name = models.CharField(verbose_name='name',max_length=256,blank=True  )
#	name_slug = models.CharField(verbose_name='Name_slug',max_length=250,blank=True)
#	lft = models.IntegerField(blank=True)
#	rght = models.IntegerField(blank=True)
#	parent = TreeForeignKey('self',null=True,blank=True,related_name='children', on_delete=models.CASCADE)

#	class MPTTMeta:
#		level_attr = 'mptt_level'
#		order_insertion_by = ['name']
#	def __unicode__(self):
#		return u"%s %s %s " %(self.name,self.name_slug,self.parent)
#	def __str__(self):
#		return u"%s %s" %(self.pk, self.name)
#	def get_children(self):
#		return Catalog.objects.filter(parent=self.pk)
#	def get_absolute_url(self):
#		return reverse("binary_view",kwargs={"slug":self.name_slug})

## test model2
class CBinary(MPTTModel):
	username = models.CharField(verbose_name='username',max_length=100,blank=True)
	parent = TreeForeignKey('self',null=True,blank=True,related_name='children', on_delete=models.CASCADE)# for ref_id
	position = models.IntegerField(null=True,blank=True)
    

	class MPTTMeta:
		level_attr = 'mptt_level'
		order_insertion_by = ['position']
	def __unicode__(self):
		return u"%s %s %s " %(self.username,self.position,self.parent)
	def __str__(self):
		return u"%s %s %s " %(self.username,self.position,self.parent)
	def get_children(self):
		return CBinary.objects.filter(parent=self.pk)

## test model3
#class Levels(MPTTModel):
#	username = models.CharField(verbose_name='username',max_length=100,blank=True  )
#	parent = TreeForeignKey('self',null=True,blank=True,related_name='children', on_delete=models.CASCADE)# for upliner
	

#	class MPTTMeta:
#		level_attr = 'mptt_level'
#		order_insertion_by = ['username']
#	def __unicode__(self):
#		return u"%s %s " %(self.username,self.parent)
#	def __str__(self):
#		return u"%s %s" %(self.username,self.parent)
#	def get_children(self):
#		return Levels.objects.filter(parent=self.pk)


# test model4
class CLevel(MPTTModel):
	username = models.CharField(verbose_name='username',max_length=100,blank=True  )
	parent = TreeForeignKey('self',null=True,blank=True,related_name='children', on_delete=models.CASCADE)# for upliner
	

	class MPTTMeta:
		level_attr = 'mptt_level'
		#order_insertion_by = ['username']
		order_insertion_by = ['id']
		ordering = ['mptt_level']

	def __unicode__(self):
		return u"%s %s " %(self.username,self.parent)
	def __str__(self):
		return u"%s %s" %(self.username,self.parent)
	def get_children(self):
		return CLevel.objects.filter(parent=self.pk)


class AccountsInfo(models.Model):
	acc_id = models.AutoField(primary_key=True)	
	customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
	acc_holder_name = models.CharField(max_length=100,blank=True) # or account holder_name
	bank_name = models.CharField(max_length=100,blank=True) 
	branch_code = models.IntegerField(null=True,blank=True) # or Routing number
	zip_code = models.IntegerField(null=True,blank=True)
	acc_number = models.IntegerField(null=True,blank=True) # bank account number/credit/debit card number/IBAN
	acc_title = models.CharField(max_length=100,blank=True)
	acc_type = models.CharField(max_length=100,blank=True) # bank account/credit/debit (should enter pin if credit card)
	acc_status = models.CharField(max_length=100,blank=True) 
	CVV = models.IntegerField(null=True,blank=True) # 3/4 digit code at the back of card
	card_expiry_date = models.DateTimeField(blank = True) # for credit/debit