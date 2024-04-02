from django.urls import path
from .views import login,employee,signup

urlpatterns = [
    path('login/',login,name='login'),
    path('employee/',employee,name='employee'),
    path('signup/',signup,name='signup'),
    
]