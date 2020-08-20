"""neighbourhood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


urlpatterns=[
    url(r'^$',views.index,name = 'index'),    
    url(r'^sendemail/$',views.send_email,name = 'send-email'),
    url(r'^create-admin/$',views.create_admin,name = 'create-admin'),
    url(r'^create-hood/$',views.create_hood,name = 'create-hood'),
    url(r'^update-hood/$',views.update_hood,name = 'update-hood'),
    url(r'^admin-profile/$',views.admin_profile,name = 'admin-profile'),
    url(r'^user-profile/$',views.user_profile,name = 'user-profile'),
    url(r'^add-occupant/$',views.add_resident,name = 'add-occupant'),
    url(r'^delete-hood/$',views.delete_hood,name = 'delete-hood'),
    url(r'^add-amenity/$',views.add_amenity,name = 'add-amenity'),
    url(r'^add-business/$',views.add_business,name = 'add-business'),
    url(r'^delete-occupant-profile/$',views.delete_resident_profile,name = 'delete-occupant-profile'),
    url(r'^change-password/$',views.change_password,name = 'change-password'),
    url(r'^make-post/$',views.make_post,name = 'make-post'),
    url(r'^occupants-list/$',views.residents_list,name = 'occupants-list'),
    url(r'^delete-occupant/(\d+)',views.delete_resident,name = 'delete-occupant'),
    url(r'^changeprofilephoto/$',views.change_profile_photo,name = 'change-profile-photo'),
]
git