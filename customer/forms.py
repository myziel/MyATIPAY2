"""
Customer Forms
Developed By : Erum Mehmood & Khalid Awan

"""
"""
CustomerForm1 and CustomerForm2 are used for signup, 
LoginForm is used for login
CPForm1 and CPForm2 are used to complete the profile
"""
from logging import PlaceHolder
from datetime import date
from django import forms
from .models import Customer, CustomerDetail, CustomerLogin
from main.models import Countries, Cities, States
from django.core.validators import validate_email



class CustomerForm1(forms.ModelForm):	
	#customer_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Customer ID'}), label = "Customer ID")
	upliner = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Upliner ID'}), label = "Upliner ID")
	ref_id = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Referral ID'}), label = "Referral ID")
	CHOICES=[('Right','Right'),
         ('Left','Left')]

	position = forms.CharField( widget=forms.Select(choices=CHOICES))
	#position = forms.CharField(widget=forms.TextInput(attrs={}))
	password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	password2  = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	username = forms.CharField(widget=forms.TextInput(attrs={'oninput':'validate()'}))
	
	#def __init__(self, *args, **kwargs):
	#	self.fields['customer_id'].widget.attrs['readonly'] = True
	#def clean_username(self):
	#	username = self.cleaned_data['username']
	#	if Customer.objects.exclude(customer_id=self.instance.customer_id).filter(username=username).exists():
	#		print(username)
	#		#self.messages.success(self, 'Username already exists!')
	#		raise forms.ValidationError(u'Username "%s" is already in use.' % username)
	#	return username

	class Meta:
		model = Customer
		fields = ['upliner', 'ref_id', 'position' , 'password1', 'password2', 'username']

	
class CustomerForm2(forms.ModelForm):	
	first_name = forms.CharField(widget=forms.TextInput(attrs={}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={}))
	#email = forms.EmailField(unique=True, validators=[validate_email,])
	class Meta:
		model = CustomerDetail
		fields = ['first_name', 'last_name']

class LoginForm(forms.ModelForm):	
	
	username = forms.CharField(widget=forms.TextInput(attrs={'oninput':'validate()'}))
	password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	
	class Meta:
		model = CustomerLogin
		fields = ['username', 'password']

class CPForm1(forms.ModelForm):	# Customer Profile Form1
	customer_id = forms.IntegerField(disabled = True , label = "Customer ID")
	upliner = forms.IntegerField(disabled = True, label = "Upliner ID")
	ref_id = forms.IntegerField(disabled = True, label = "Referral ID")
	CHOICES=[('Right','Right'),
         ('Left','Left')]

	position = forms.CharField(disabled = True)
	username = forms.CharField(disabled = True)
	

	class Meta:
		model = Customer
		fields = ['customer_id', 'upliner', 'ref_id', 'position', 'username']

	
class CPForm2(forms.ModelForm):	# Customer Profile Form2
	first_name = forms.CharField(widget=forms.TextInput(attrs={}), label = "First Name")
	last_name = forms.CharField(widget=forms.TextInput(attrs={}), label = "Last Name")
	country = forms.ModelChoiceField(queryset=Countries.objects.all())
	email = forms.EmailField(validators=[validate_email,])
	photo = forms.ImageField(required = False)
	mobile = forms.CharField(widget=forms.TextInput(attrs={}))
	alternate_mobile = forms.CharField(widget=forms.TextInput(attrs={}))
	address = forms.CharField(widget=forms.TextInput(attrs={}))
	zipcode = forms.CharField(widget=forms.TextInput(attrs={}))
	#city = forms.ModelChoiceField(queryset=Cities.objects.none()) # empty cities combo box
	#state = forms.ModelChoiceField(queryset=States.objects.none()) # empty states combo box
	GENDER_CHOICES = (("Male",'Male'),("Female",'Female'),("Other",'Other'))
	gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
	year_limit = date.today().year - 18
	dob = forms.DateField(widget=forms.SelectDateWidget(years=range(year_limit, 1901, -1)),label = "Date of Birth")
	cnic = forms.CharField(widget=forms.TextInput(attrs={}), label = "CNIC")# write cnic validator
	#def __init__(self, *args, **kwargs):
	#	super(CPForm2, self).__init__(*args, **kwargs)
	#	if self.is_bound:
	#		country_obj = self.fields['country'].clean(self.data.get('country'))
	#		print(country_obj)
	#		self.fields['state'] = forms.ModelChoiceField(queryset=States.objects.filter(country_id=country_obj))
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		#self.fields['country'].queryset = Country.objects.none()
		self.fields['state'].queryset = States.objects.none()
		self.fields['city'].queryset = Cities.objects.none()
		print(self.instance.country_id)
		if 'country' in self.data:
			try:
				country_id = int(self.data.get('country'))
				self.fields['state'].queryset = States.objects.filter(country_id=country_id).order_by('state')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.country_id:
			self.fields['state'].queryset = States.objects.filter(country_id=self.instance.country_id).order_by('state')

		if 'country' in self.data and 'state' in self.data:
			try:
				country_id = int(self.data.get('country'))
				state_id = int(self.data.get('state'))
				self.fields['city'].queryset = Cities.objects.filter(country_id=country_id, state_id=state_id).order_by('city')
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.state_id:
			self.fields['city'].queryset = Cities.objects.filter(country_id=self.instance.country_id, state_id=self.instance.state_id).order_by('city')
		
		

	class Meta:
		model = CustomerDetail
		fields = ['first_name', 'last_name', 'email', 'photo','mobile', 'country',
			'alternate_mobile', 'address', 'zipcode', 'city', 'state', 'gender', 'dob', 'cnic']


	
