"""
Customer Views
Developed By : Erum Mehmood & Khalid Awan

"""
from django.shortcuts import render, HttpResponse, redirect
from . import forms,models
from main.models import Countries, Cities, States
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from urllib.parse import urlencode
from django.contrib import messages
from datetime import date, datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#def indexView(request):
#    return render(request,'customer/index.html')

# customer signup
def cSignup(request):
    form1=forms.CustomerForm1()
    form2=forms.CustomerForm2()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        #print('valid if')
        form1=forms.CustomerForm1(request.POST)
        form2=forms.CustomerForm2(request.POST)
        # put checks for upliner....suggest upliner 1 while form load
        if form1.is_valid() and form2.is_valid():
            #print('valid')
            # check if username already exists:
            username = form1.cleaned_data.get('username')
            #customer_id = form1.cleaned_data.get('customer_id')
            #if models.Customer.objects.exclude(customer_id=customer_id).filter(username=username).exists():
            #    print("usernmae exists")
            #    messages.success(request, 'Username already exists!')
            #    return redirect('cSignup')
                #return render(request,'customer/cSignup.html',context=mydict)
            
            password = form1.cleaned_data.get('password1')
            # get list of all exisitng customer_ids
            # check if ref_ids and upliner are from existing customer_ids "This customer_id doesnt exist"
            # and if ref_id is 0 or 1 then allow to include otherwise display message "This refferal id is already occupied, 
            # next available id in binary is -----"

            upliner = form1.cleaned_data.get('upliner')
            if models.Customer.objects.filter(customer_id=upliner).exists():
                print("Upliner exists")
            else:
                messages.success(request, "This upliner doesn't exist!\nIf you don't know any upliner, input 1.")
                return redirect('cSignup')
            
            ref_id = form1.cleaned_data.get('ref_id')
            
            if models.Customer.objects.filter(customer_id=ref_id).exists():
                print("ref_id exists")
            else:
                messages.success(request, "This ref_id doesn't exist!")
                return redirect('cSignup')
            

            position = form1.cleaned_data.get('position')
            # check if both left right positions of input ref_id are occupied or available
            # show the next availabe ref_id under upliner subtrees.............
            customers = models.Customer.objects.filter(ref_id=ref_id)
            if customers.count() == 2:
                messages.success(request, "Both positions of this ref_id are occupied!")
                return redirect('cSignup')
                
            elif customers.count() == 1:
                # check if input position is already taken for input ref_id
                if customers[0].position == position:
                    messages.success(request, position+" position of this ref_id is occupied!")
                    return redirect('cSignup')
                
            
            encryptedpassword=make_password(password)
            #print(encryptedpassword)
            customer=form1.save(commit=False)
            #customer.customer_id = customer_id
            customer.password = encryptedpassword
            customer.save()

            # save same data into CBinary Model , storing 0 for left position, and 1 for right position
            if position == "Right":
                posInt = 1 
            elif position == "Left":
                posInt = 0
            models.CBinary.objects.create(username = username, parent_id=ref_id, position=posInt)

            # save same data into CLevel Model
            models.CLevel.objects.create(username = username, parent_id=upliner)

            customer_d=form2.save(commit=False)
            #customer_d.customer_id = customer_id
            customer_d.save()   
            first_name = form2.cleaned_data.get('first_name')
            last_name = form2.cleaned_data.get('last_name')
            #position = form1.cleaned_data.get('position')
            #print(userForm.cleaned_data)            
            #The save() method accept an optional keyword argument commit which is either True or False . If we call save() with commit=False ,
            #it will return an object that is not save in database , which is useful to do custom processing before saving .            
            
            #my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            #my_customer_group[0].user_set.add(user)
            #return redirect('successful', id = customer.customer_id,  login_id = 1, state='s')
            context = {'customer_id':customer.customer_id, 'first_name':first_name, 'last_name':last_name, 'username':username}
            return render(request,'customer/cSuccessful.html',context=context)
        else:
            errorLst = ''
            print(form1.errors.items())
            print('username' in form1.errors.as_data().keys())
            print(form2.errors.items())
            
            if 'username' in form1.errors.as_data().keys():
                errorLst = 'Customer with this username already exists!'
            else:
                errorLst = form1.errors()
            print(errorLst)
            messages.success(request, errorLst)
            return redirect('cSignup')
        
    else:
        form1=forms.CustomerForm1()
        form2=forms.CustomerForm2()

    return render(request,'customer/cSignup.html',context=mydict)



def cLogin(request):
    
    loginform=forms.LoginForm()
    mydict={'loginform':loginform}
    if request.method == 'POST':

        loginform=forms.LoginForm(request.POST)
        if loginform.is_valid():
            
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            login = loginform.save(commit=False)
            # get ip address
            user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
            if user_ip_address:
                ip = user_ip_address.split(',')[0] 
            else:
                ip = request.META.get('REMOTE_ADDR')
            
             # fetch password from customer model based on input username
            customer = models.Customer.objects.get(username = username)
            # fetch today's login count for customer_id
            today_login_customer = models.CustomerLogin.objects.filter(customer_id = customer.customer_id,
                                                                        login_date = date.today())
            #print("Today Count: ", today_login_customer.count())
           

            if customer == None:
                print("Username doesn't exist!")
            else:
                # compare input password with stored password
                checkpassword=check_password(password, customer.password)
                #print(checkpassword)
                # if password matches, save login form after saving customer_id and ip address in the corresponding fields
                if checkpassword:
                    login.customer_id = customer.customer_id
                    login.ip = ip
                    login.is_now_login = True
                    login.today_login_attempt += today_login_customer.count()
                    login.save()
                    binaryObject =nodes= models.CBinary.objects.filter(pk=customer.customer_id)[0]
                    #base_url = reverse('customerhomepage')  # 1 /products/
                    #query_string =  urlencode({'id': customer.customer_id})  # 2 category=42
                    #url = '{}?{}'.format(base_url, query_string)  # 3 /products/?category=42
                    #return redirect(url)
                    request.session['login_customer_id'] = customer.customer_id
                    request.session['login_id'] = login.login_id
                    return redirect('cHomepage', id = customer.customer_id, login_id = login.login_id, o_mptt_level = binaryObject.mptt_level)
                else:
                    # save details for wrong login attempt if password is incorrect
                    login.customer_id = customer.customer_id
                    login.ip = ip
                    login.is_now_login = False
                    login.wrong_login_attempt = 1
                    # fecth customer details from login model for login time of last 30 mins
                    limit = 30
                    now = datetime.now()            
                    max_time = now -  timedelta(minutes=limit)
                    #max_time = max_time.strftime("%H:%M:%S")
                    login_customer = models.CustomerLogin.objects.filter(customer_id = customer.customer_id,
                                                                        login_time__gte = max_time,
                                                                        login_time__lte = now,
                                                                        wrong_login_attempt__gte = 1)                   

                    
                    login.today_login_attempt += today_login_customer.count()
                    login.wrong_login_attempt += login_customer.count()
                    login.save()
                    messages.success(request,"Wrong Password! Attempt: " + str(login.wrong_login_attempt) + " in last " + str(limit) + " minutes.")

                    
                    #print("Max_time: ", max_time, " Count: ", login_customer.count())
                    # return if 3 wrong login attempts in last 1 minute
                    #if login_customer.count() == 1:
                    #    messages.success(request,"3 wrong login attempts in last " + str(limit) + " minute!")
                    #    return render(request, 'customer/cLogin.html', context=mydict)
        else:

            print(loginform.errors)
    else:
        loginform = forms.LoginForm()
    return render(request, 'customer/cLogin.html', context=mydict)

def cDashboard(request):
    # show customer full name, id, referral id, upliner id, position
    return render(request, 'customer/cDashboard.html')

#@login_required(login_url='customerlogin')
#@user_passes_test(is_customer)

def cHomepage(request, id, login_id, o_mptt_level):
    login_customer_id = request.session.get('login_customer_id')
    #print(login_customer_id)
    customer = models.Customer.objects.get(customer_id = login_customer_id)# customer_id
    customerDetail = models.CustomerDetail.objects.get(customer_id = login_customer_id)
    username = customer.username
    ref_id = customer.ref_id
    upliner = customer.upliner
    position = customer.position
    first_name = customerDetail.first_name
    last_name = customerDetail.last_name
    request.session['first_name'] = first_name
    request.session['last_name'] = last_name
    #print(username)
    context = {'customer':customerDetail, 'customer_id': id, 'username':username, 
                'first_name':first_name, 'last_name':last_name, 'upliner':upliner, 'ref_id': ref_id,
                'position':position, 'login_id':login_id, 'o_mptt_level':o_mptt_level}

    return render(request,'customer/cHome.html',context = context)


def cProfile(request, id, login_id, o_mptt_level):
    #fetch customer details after confirming if he is still login
    customer = models.Customer.objects.get(customer_id = id)# customer_id
    customerDetail = models.CustomerDetail.objects.get(customer_id = id)
    username = customer.username
    ref_id = customer.ref_id
    upliner = customer.upliner
    position = customer.position
    first_name = customerDetail.first_name
    last_name = customerDetail.last_name
    
    form1=forms.CPForm1(instance=customer)
    form2=forms.CPForm2(instance=customerDetail)
    mydict = {'customer':customerDetail, 'customer_id': id,'username':username, 
                'first_name':first_name, 'last_name':last_name, 'upliner':upliner, 'ref_id': ref_id,
                'position':position, 'login_id':login_id, 'form1':form1,'form2':form2, 'o_mptt_level':o_mptt_level}
    #form2 = forms.CPForm2(request.country_id, request.POST)
    #print(request.GET.get('country').selected())
    #form2.fields['state'].queryset = States.objects.filter(country_id=request.country_id)
    
    if request.method=='POST':
        #print('valid if')
        form1=forms.CPForm1(request.POST)
        form2=forms.CPForm2(request.POST, instance=customerDetail)
        #print(form2)
        #print('selected state: ', form2.fields['state'])#.get('state_id'))
        if form2.is_valid():
            user = form2.save(commit=False)
            #customerDetail.first_name = form2.cleaned_data.get('first_name')
            #customerDetail.last_name = form2.cleaned_data.get('last_name')
            #customerDetail.email = form2.cleaned_data.get('email')
            #customerDetail.dob = form2.cleaned_data.get('dob')
            #customerDetail.photo = form2.cleaned_data.get('photo')
            #customerDetail.city = form2.cleaned_data.get('city')
            #customerDetail.cnic = form2.cleaned_data.get('cnic')
            #if form2.cleaned_data.get('country'):
            #    print("country id:",form2.cleaned_data.get('country'))
            #    customerDetail.country = form2.cleaned_data.get('country')
            #if form2.cleaned_data.get('state'):
            #    customerDetail.country = form2.cleaned_data.get('state')
            #if form2.cleaned_data.get('city'):
            #    customerDetail.country = form2.cleaned_data.get('city')

            #customerDetail.photo = form2.cleaned_data.get('photo')
            user.save()
            messages.success(request, 'Profile details updated.')
            user.refresh_from_db()
            return redirect('cHomepage', id = id, login_id = login_id, o_mptt_level=o_mptt_level)
        else:
            print("Errors: ", form2.errors)
            print()
    else:
        print('Errors', request.GET)
        
    return render(request, 'customer/cProfile.html', context=mydict)

def cLogout(request):
    login_customer_id = request.session.get('login_customer_id')
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    login_customer = models.CustomerLogin.objects.filter(customer_id = login_customer_id)
    for each in login_customer:
        #print(each)
        each.is_now_login = False
        #print(each.is_now_login)
        each.save()
    context = {'first_name':first_name, 'last_name':last_name}
    try:
        del request.session['login_customer_id']
    except KeyError:
        pass
    #return HttpResponse("You're logged out.")
    return render(request, 'customer/cLogout.html', context = context)


def load_cities(request):
    country_id = request.GET.get('country')
    state_id = request.GET.get('state')
    print('load state view: ', country_id)
    print('load citie view: ', state_id)
    cities = Cities.objects.filter(country_id=country_id , state_id=state_id).order_by('city')
    #print(cities)
    return render(request, 'customer/city_dropdown_list_options.html', {'cities': cities})

def load_states(request):
    country_id = request.GET.get('country')
    #print('load state view: ', country_id)
    states = States.objects.filter(country_id=country_id).order_by('state')
    #print("States from view: ",states)
    #cities = Cities.objects.filter(country_id=0)# , state_id=state_id).order_by('city')
    return render(request, 'customer/state_dropdown_list_options.html', {'states':states})#, 'cities':cities})


'''
binary_view 
@params
    id holds customer id whenever any node is clicked to be spreaded
    customer_id preserves id through wich user is logged in
    mptt_level is the level of clicked node
    o_mptt_level is level of logged in user
    login_id is login id
only two levels are shown for binary tree at one time
'''
def binary_view(request, id, o_mptt_level, mptt_level, customer_id, login_id):
    login_customer_id = request.session.get('login_customer_id')
    customer = models.Customer.objects.all().values()#.get(customer_id = login_customer_id)# customer_id
    customerDetail = models.CustomerDetail.objects.all().values()#.get(customer_id = login_customer_id)
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    nodes = models.CBinary.objects.filter(pk=id)
    first = nodes[0]
    count = first.get_descendants().count()
    
    '''
    page = request.GET.get('page', 1)
    # making 10 pages for customer detail table data
    paginator = Paginator(customerDetail, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    '''
    context = {'nodes':nodes, 'id':id, 'login_id':login_id, 
               'customer_id':customer_id, 'mptt_level':mptt_level+2, 
               'o_mptt_level':o_mptt_level, 'count':count, 'first_name':first_name, 
               'last_name':last_name, 'customer':customer, 'customerDetail':customerDetail}

    return render(request, 'customer/cBinary.html', context = context)

'''
level_view 
@params
    id holds customer id whenever any node is clicked to be spreaded
    customer_id preserves id through wich user is logged in
    mptt_level is the level of clicked node
    o_mptt_level is level of logged in user
    login_id is login id
'''
def level_view(request,  id, o_mptt_level, mptt_level, customer_id, login_id):
    #nodes = models.CLevel.objects.all()
    #print(id)
    customer = models.Customer.objects.all().values()#.get(customer_id = login_customer_id)# customer_id
    customerDetail = models.CustomerDetail.objects.all().values()#.get(customer_id = login_customer_id)
    first_name = request.session.get('first_name')
    last_name = request.session.get('last_name')
    nodes = models.CLevel.objects.filter(pk=id)
    count = nodes[0].get_descendants().count()
    mptt_level = nodes[0].mptt_level + 1
    context = {'nodes':nodes, 'id':id, 'login_id':login_id, 'customer_id':customer_id, 'mptt_level':mptt_level, 
               'o_mptt_level':o_mptt_level, 'count':count , 'first_name':first_name, 'last_name':last_name,
              'customer':customer, 'customerDetail':customerDetail}
    return render(request, 'customer/cLevel.html', context = context)


'''
simple logout using del session
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
The standard django.contrib.auth.logout() function actually does a bit more than this to prevent inadvertent data leakage. 
It calls the flush() method of request.session. We are using this example as a demonstration of how to work with session objects, 
not as a full logout() implementation.
'''


