from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from sec import views as sec_views
from users import views as users_views

#last work in addpers if  you dont remember 
urlpatterns = [
    path('', users_views.calendar, name='home'),
    path('addpers/',sec_views.add_pers, name='addpers'),
    path('admin/', admin.site.urls),
    path('personel/', sec_views.personel,name='personel'),
    path('materiel/',sec_views.materiel, name='materiel'),
    path('register/',users_views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('profile/', users_views.profile, name= 'profile'),
    path('add_event/', users_views.add_event, name='add_event'),
    path('update/', users_views.update, name='update'),
    path('remove/', users_views.remove, name='remove'),
   
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)