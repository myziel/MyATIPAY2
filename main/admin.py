from django.contrib import admin
from .models import Countries, States, Cities
from customer.models import Customer, CustomerDetail, CustomerLogin, CBinary, CLevel
# Register your models here.

admin.site.site_header = 'MyATIPAY'

#admin.site.register(EndUser)
#admin.site.register(FinancialDetail)
admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(Customer)
admin.site.register(CustomerDetail)
admin.site.register(CustomerLogin)
# test models registration
admin.site.register(CBinary)
admin.site.register(CLevel)
