"""
Main Forms
Developed By : Erum Mehmood & Khalid Awan

"""
from django import forms
#from .models import EndUser
from customer.models import CustomerDetail

#class UserForm(forms.ModelForm):	
#	user_id = forms.IntegerField(widget=forms.TextInput(attrs={}))
#	first_name = forms.CharField(widget=forms.TextInput(attrs={}))
#	last_name = forms.CharField(widget=forms.TextInput(attrs={}))
#	username = forms.CharField(widget=forms.TextInput(attrs={'oninput':'validate()'}))
	
#	class Meta:
#		model = EndUser
#		fields = ['user_id', 'first_name', 'last_name', 'username']

	
#class CustomerForm(forms.ModelForm):	
#	upliner = forms.IntegerField(widget=forms.TextInput(attrs={}))
#	ref_id = forms.IntegerField(widget=forms.TextInput(attrs={}))
#	CHOICES=[('Right','Right'),
#         ('Left','Left')]

#	position = forms.CharField( widget=forms.Select(choices=CHOICES))
#	#position = forms.CharField(widget=forms.TextInput(attrs={}))
#	password1 = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
#	password2  = forms.CharField(label=("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={}),)
	
#	class Meta:
#		model = CustomerDetail
#		fields = ['upliner', 'ref_id', 'position' , 'password1', 'password2']