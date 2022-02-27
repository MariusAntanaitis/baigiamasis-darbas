"""baigiamasis_darbas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from pradziamokslis.views import HomepageView, MathView, StudentsListView, MokinysCreateView, MokinysUpdateView, MokinysDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='home'),
    path('mokiniai/', StudentsListView.as_view(), name='students_list'),
    path('math/', MathView.as_view(), name='math'),
    path('mokinys/create', MokinysCreateView.as_view()),
    path('mokinys/<pk>/update', MokinysUpdateView.as_view(), name="mokinys_update"),
    path('mokinys/<pk>/delete', MokinysDeleteView.as_view(), name="mokinys_delete")
]
