"""
Main urls
Developed By : Erum Mehmood & Khalid Awan

"""
from django.urls import path
from . import views
from customer import views as customer_views

urlpatterns = [
    path('', views.index, name='home'),
    path('cSignup/', customer_views.cSignup, name='cSignup'),
    path('cLogin', customer_views.cLogin ,name='cLogin'),
    path('cDashboard/', customer_views.cDashboard ,name='cDashboard'),
    path('cLogout/', customer_views.cLogout ,name='cLogout'),
    path('binary_view/<int:id>/<int:customer_id>/<int:o_mptt_level>/<int:mptt_level>/<int:login_id>/', customer_views.binary_view ,name='binary_view'),
    path('level_view/<int:id>/<int:customer_id>/<int:o_mptt_level>/<int:mptt_level>/<int:login_id>/', customer_views.level_view ,name='level_view'),
    path('cHomepage/<int:id>/<int:login_id>/<int:o_mptt_level>/', customer_views.cHomepage ,name='cHomepage'),
    path('cProfile/<int:id>/<int:login_id>/<int:o_mptt_level>/', customer_views.cProfile ,name='cProfile'),
    path('ajax/load-states/', customer_views.load_states, name='ajax_load_states'),
    path('ajax/load-cities/', customer_views.load_cities, name='ajax_load_cities'),
    #path('customerhomepage/(?P<id>[0-9]+)/$', customer_views.customer_home_view ,name='customerhomepage'),

]