"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('Swiggy_Corporate/', views.Swiggy_Corporate, name='Swiggy_Corporate'),
    path('partner_with_us/', views.partner_with_us, name='partner_with_us'),
    path('swiggy_neb/', views.swiggy_neb, name='swiggy_neb'),
    path("Our_Businesses/",views.Our_Businesses, name="Our_Businesses"),
    path("Delivering/",views.Delivering, name="Delivering"),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login,name='login'),
    # path('login/dashboard/',views.dashboard,name='dashboard'),
    path('logout/', views.logout,name='logout'),
    path('desshboard2/', views.desshboard2, name='desshboard2'),
    path('login/dashboard/query/', views.query,name='query'),
    path('login/dashboard/querydata/',views.querydata,name='querydata'),
    path('login/dashboard/showquery/',views.showquery,name='showquery'),
    path('login/dashboard/showquery/delete/<int:qpk>/',views.delete,name='delete'),
    path('login/dashboard/showquery/edit/<int:qpk>/',views.edit,name='edit'),
    path('login/dashboard/showquery/update/<int:qpk>/',views.update,name='update'),
    path('login/dashboard/search/', views.search,name='search'),
    path('addcart/<int:pk>/',views.addcart,name='addcart')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


