from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),
    path('article/', views.article, name='article'),  # This is the correct path for the article page
    path('contact/', views.contact, name='contact'),
    
    path('blogs/', views.blogs, name='blogs'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    
    path('usertrainer/', views.usertrainer, name='usertrainer'),
    path('gender/', views.gender, name='gender'),
    path('bmi/', views.bmi, name='bmi'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('videocallfun/', views.videocallfun, name='videocallfun'),
    path('videocall/', views.videocall, name='videocall'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('ashok/', views.ashok, name='ashok'),
    path('rahul/', views.rahul, name='rahul'),
    path('protinecal/', views.protinecal, name='protinecal'),
    path('contactus/', views.contactus, name='contactus'),
    path('joinvideocall/', views.joinvideocall, name='joinvideocall'),
    
# Add these to your existing urlpatterns
path('user-information/', views.user_information_form, name='user_information_form'),
path('user-information/display/', views.user_information_display, name='user_information_display'),
path('user-information/edit/', views.user_information_edit, name='user_information_edit'),
    
    
]


