"""
Main views
Developed By : Erum Mehmood & Khalid Awan

"""
from django.contrib.auth import login, authenticate
from . import forms,models
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password

# home page
def index(request):
    return render(request, 'main/index.html')

# customer signup
def signup(request):
    userForm=forms.UserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        #print('valid if')
        userForm=forms.UserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            #print('valid')
            models.EndUser=userForm.save()
            #user.set_password(user.password)
            models.EndUser.save()
            #EndUser.refresh_from_db()
            #print(models.EndUser)
            user_id = userForm.cleaned_data.get('user_id')
            position = customerForm.cleaned_data.get('position')
            password = customerForm.cleaned_data.get('password1')
            #print(userForm.cleaned_data)
            #print(customerForm.cleaned_data)
            #print(password)
            
            customer=customerForm.save(commit=False)
            
            '''
            The save() method accept an optional keyword argument commit which is either True or False . If we call save() with commit=False ,
           it will return an object that is not save in database , which is useful to do custom processing before saving .
            '''
            encryptedpassword=make_password(password)
            print(encryptedpassword)
            customer.password = encryptedpassword
            #checkpassword=check_password(password, encryptedpassword) # for decryptpassword
            #print(checkpassword)
            customer.user_id = models.EndUser.user_id
            customer.save()
            #my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            #my_customer_group[0].user_set.add(user)
        else:
            print(userForm.errors)
            print(customerForm.errors)
        return redirect('customer/customerdashboard.html')
    else:
        userForm=forms.UserForm()
        customerForm=forms.CustomerForm()

    return render(request,'main/customersignup.html',context=mydict)
    #    userForm = SignUpForm(request.POST)
    #    customerForm = CustomerSignUpForm(request.POST)
    #    mydict={'userForm':userForm,'customerForm':customerForm}
    #    if userForm.is_valid() and customerForm.is_valid():
    #        userForm.save()
    #        customerForm.save()
    #        #user_id = signupform.cleaned_data.get('user_id')
    #        #upliner = customersignupform.cleaned_data.get('upliner')
    #        #ref_id = customersignupform.cleaned_data.get('ref_id')
    #        #position = customersignupform.cleaned_data.get('position')
    #        #first_name = signupform.cleaned_data.get('first_name')
    #        #last_name = signupform.cleaned_data.get('last_name')
    #        #username = signupform.cleaned_data.get('username')
    #        #password1 = customersignupform.cleaned_data.get('password1')
    #        #password2 = customersignupform.cleaned_data.get('password2')
    #        #print(username)
    #        #user = authenticate(user_id=user_id, position=position, username=username, first_name=first_name, last_name=last_name, password=password1, upliner=upliner, ref_id=ref_id)
    #        #login(request, user)
    #        return HttpResponseRedirect('/thanks/')
    #    else:
    #        return redirect('home')
    #else:
    #    signUpForm = SignUpForm()
    #return render(request, 'main/signup.html', context=mydict)
